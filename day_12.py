from aocd.models import Puzzle
from collections import defaultdict


def get_data():
    puzzle = Puzzle(year=2021, day=12)
    data = puzzle.input_data
    data = [[y for y in x.split("-")] for x in data.split("\n")]
    dataset = defaultdict(list)

    for x in data:
        dataset[x[0]].append(x[1])
        dataset[x[1]].append(x[0])
    return dataset


def visit(p, node, visited, part):
    res = []
    new_visit = visited + [node]
    if node == "end":
        return[new_visit]
    for n in p[node]:
        if n != 'start':
            if part == 1:
                if n not in visited or n.isupper():
                    temp_res = visit(p, n, new_visit, part)
                    res.extend(temp_res)
            if part == 2:
                if n.isupper():
                    temp_res = visit(p, n, new_visit, part)
                    res.extend(temp_res)
                else:
                    l_case = [i for i in new_visit if i.islower()]
                    twice = any([True for i in l_case if l_case.count(i) > 1])
                    if (twice and new_visit.count(n) < 1) or (not twice and new_visit.count(n) < 2):
                        temp_res = visit(p, n, new_visit, part)
                        res.extend(temp_res)
    return res


d = get_data()

print("Part 1 answer is: ", len(visit(d, 'start', [], 1)))
print("Part 2 answer is: ", len(visit(d, 'start', [], 2)))
