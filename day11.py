from aocd.models import Puzzle

number_of_flash = 0
list_of_9 = []


def get_data():
    puzzle = Puzzle(year=2021, day=11)
    data = puzzle.input_data
    data = [[int(y) for y in x] for x in data.split("\n")]
    height = len(data)
    width = len(data[0])
    return data, height, width

data, height, width = get_data()


def compare(rr, cc):
    global list_of_9
    dr = [1, 0, -1, 0, -1, -1, 1, 1]
    dc = [0, 1, 0, -1, -1, 1, 1, -1]
    if data[rr][cc] == 10:
        list_of_9.append((rr, cc))
        for i in range(8):
            rr2, cc2 = rr + dr[i], cc + dc[i]
            if 0 <= rr2 < height and 0 <= cc2 < width:
                data[rr2][cc2] += 1
                if data[rr2][cc2] == 10:
                    list_of_9.append((rr2, cc2))
                    compare(rr2, cc2)


def compare_all():
    global list_of_9
    no_of_flash_to_append = 0
    for x in range(height):
        for y in range(width):
            data[x][y] += 1
            compare(x, y)
    list_of_9 = set(list_of_9)
    for num in list_of_9:
        data[num[0]][num[1]] = 0
        no_of_flash_to_append += 1
    return no_of_flash_to_append


def part1():
    global list_of_9
    number_of_flash = 0
    for request in range(100):
        list_of_9 = []
        number_of_flash += compare_all()
    return number_of_flash


def part2():
    global data, height, width, list_of_9
    data, height, width = get_data()
    count0 = True
    step = 0
    while count0:
        list_of_9 = []
        compare_all()
        step += 1
        if len(list_of_9) == 100:
            count0 = False
    return step


print(f"Part 1 answer is: {part1()}")
print(f"Part 2 answer is: {part2()}")
