from aocd.models import Puzzle
import heapq
from collections import defaultdict


def get_data():
    puzzle = Puzzle(year=2021, day=15)
    dataset = puzzle.input_data
    return dataset


def solve(tiles):
    rows, cols = size_y * tiles, size_x * tiles
    costs = defaultdict(int)

    pqueue = [(0, 0, 0)]
    heapq.heapify(pqueue)
    visited = set()
    while len(pqueue) > 0:
        cost, row, col = heapq.heappop(pqueue)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        costs[(row, col)] = cost
        if row == rows - 1 and col == cols - 1:
            break

        for mv_y, mv_x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row = row + mv_y
            new_col = col + mv_x
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                continue

            new_cost = ((data[new_row % size_y][new_col % size_x]
                                       + (new_row // size_y)
                                       + (new_col // size_x))
                        - 1
                       ) % 9 + 1
            heapq.heappush(pqueue, (cost + new_cost, new_row, new_col))
    return costs[(rows - 1, cols - 1)]


data = get_data()
data = [[int(y) for y in x] for x in data.split("\n")]
size_y, size_x = len(data), len(data[0])

print(f"Part 1 answer is: {solve(1)}")
print(f"Part 2 answer is: {solve(5)}")
