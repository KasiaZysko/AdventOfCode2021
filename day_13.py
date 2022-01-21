from aocd.models import Puzzle
global points_last


def get_data():
    puzzle = Puzzle(year=2021, day=13)
    dataset = puzzle.input_data
    dataset = [x for x in dataset.split("\n")]

    index = dataset[0:dataset.index("")]
    index = [x.split(",") for x in index]
    index = [[int(x) for x in y] for y in index]
    folding_set = [x.replace("fold along ", "") for x in dataset[dataset.index("") + 1:]]
    folding_set = [x.split("=") for x in folding_set]
    return dataset, folding_set, index


def fold(index_of_cor, number):
    global points_last
    points = []
    for x in indexes:
        if x[index_of_cor] >= number:
            difference = number*2 + 1
            x[index_of_cor] = difference - x[index_of_cor] - 1
            points.append((x[0], x[1]))
        else:
            points.append((x[0], x[1]))
    points_last = set(points)


def part_1():
    for i in folding:
        if i[0] == "x":
            n = 0
        else:
            n = 1
        fold(n, int(i[1]))
        if folding.index(i) == 0:
            print(f"Part 1 answer is: {len(points_last)}")


def part_2():
    last_call = [[" " for x in range(50)] for y in range(15)]
    for x in points_last:
        last_call[x[1]][x[0]] = "#"
    for x in last_call:
        print("".join(x))


data, folding, indexes = get_data()
part_1()
print("Part 2 answer is: ")
part_2()

