from aocd.models import Puzzle


def get_puzzle():
    puzzle = Puzzle(year=2021, day=2)
    data = puzzle.input_data
    data_split = [line for line in data.split("\n")]
    return data_split


def puzzle_result():
    horizontal, vertical, aim, vertical2 = 0, 0, 0, 0
    for line in numbers:
        position = line.split()[0]
        value = int(line.split()[1])
        if position == "forward":
            horizontal += value
            vertical2 += aim * value
        elif position == "down":
            vertical += value
            aim += value
        elif position == "up":
            vertical -= value
            aim -= value
    return horizontal, vertical, vertical2


numbers = get_puzzle()
hor, ver, ver2 = puzzle_result()
print(f"Part 1 answer is: {hor*ver}")
print(f"Part 2 answer is: {hor*ver2}")
