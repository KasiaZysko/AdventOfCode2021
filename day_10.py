from aocd.models import Puzzle

puzzle = Puzzle(year=2021, day=10)
data = puzzle.input_data
data = data.split("\n")

data_lines = ['[}', '[)', '[>',
              '{)', '{>', '{]',
              '(>', '(}', '(]',
              '<)', '<}', '<]']

values = {")": 3, "]": 57, "}": 1197, ">": 25137}
values2 = {"(": 1, "[": 2, "{": 3, "<": 4}
counting = 0
counting2 = []

for x in data:
    new = x
    while "()" in new or "[]" in new or "{}" in new or "<>" in new:
        new = new.replace("()", "").replace("[]", "").replace("{}", "").replace("<>", "")

    for n in data_lines:
        if n in new:
            counting += values[n[1]]
            new = ""

    if ")" in new or "]" in new or "}" in new or ">" in new:
        pass
    else:
        if len(new) > 0:
            value = 0
            for y in range(len(new) - 1, -1, -1):
                value *= 5
                value += values2[new[y]]
            counting2.append(value)

print(f"Part 1 answer is: {counting}")
counting2.sort()
print(f"Part 2 answer is: {counting2[round(len(counting2) / 2)]}")
