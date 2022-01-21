from aocd.models import Puzzle


def get_data():
    puzzle = Puzzle(year=2021, day=9)
    dataset = puzzle.input_data.split("\n")
    return [[int(x) for x in y] for y in dataset]


def compare(r, c):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    lowpoint = True
    for i in range(4):
        rr, cc = r + dr[i], c + dc[i]
        if 0 <= rr < height and 0 <= cc < width:
            if data[r][c] >= data[rr][cc]:
                lowpoint = False
    return lowpoint


def compare_rek(r, c, basin):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    newpoints = set()
    for i in range(4):
        rr, cc = r + dr[i], c + dc[i]
        if (rr, cc) not in basin and rr >= 0 and cc >= 0 and rr < height and cc < width and data[rr][cc] < 9:
            newpoints.add((rr, cc))
    basin = basin.union(newpoints)
    for np in newpoints:
        basin = basin.union(compare_rek(np[0], np[1], basin))
    return basin


def part_1():
    risk_lvl = 0
    for r in range(height):
        for c in range(width):
            if compare(r, c):
                low_points.add((r, c))
                risk_lvl += 1 + data[r][c]
    return risk_lvl


def part_2():
    basins = []
    for r, c in low_points:
        basins += [len(compare_rek(r, c, {(r, c)}))]
    prod = 1
    for i in range(3):
        maximum = max(basins)
        basins.remove(maximum)
        prod *= maximum
    return prod


data = get_data()
height = len(data)
width = len(data[0])
low_points = set()

print(f"Part 1 answer is: {part_1()}")
print(f"Part 2 answer is: {part_2()}")
