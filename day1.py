from aocd.models import Puzzle


def get_puzzle():
    puzzle = Puzzle(year=2021, day=1)
    data = puzzle.input_data
    data_split = [int(line) for line in data.split()]
    return data_split


def part1():
    number_of_increase = 0
    for num in range(2, len(numbers)):
        if numbers[num] > numbers[num-1]:
            number_of_increase += 1
    return number_of_increase


def part2():
    number_of_increase = 0
    for num in range(3, len(numbers)):
        sum1 = [sum(numbers[num-3:num])]
        sum2 = [sum(numbers[num-2:num+1])]
        if sum2 > sum1:
            number_of_increase += 1
    return number_of_increase


numbers = get_puzzle()
print(f"Part 1 answer is: {part1()}")
print(f"Part 2 answer is: {part2()}")