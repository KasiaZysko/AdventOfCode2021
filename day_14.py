from aocd.models import Puzzle
from collections import Counter


def get_data():
    puzzle = Puzzle(year=2021, day=14)
    data = puzzle.input_data
    data = [x for x in data.split("\n")]
    line_of_text_data = data[0]
    pairs_data = Counter()
    rules_data = {}
    for x in range(len(line_of_text_data) - 1):
        pairs_data["".join(line_of_text_data[x:x + 2])] += 1
    for i in data[2:]:
        x = i.split(" -> ")
        rules_data[x[0]] = x[1][0]
    return line_of_text_data, pairs_data, rules_data


def calculate_result(line_of_text, pairs, steps):
    for step in range(steps + 1):
        # count all letters
        if step == steps:
            letters = Counter()
            for pair in pairs:
                letters[pair[0]] += pairs[pair]
            letters[line_of_text[-1]] += 1
            most_common_value = max(Counter(letters).most_common(1))[1]
            least_common_value = Counter(letters).most_common()[-1][1]
            return most_common_value - least_common_value
        # add all new pairs
        new_pairs = Counter()
        for pair in pairs:
            new_pairs[pair[0] + rules[pair]] += pairs[pair]
            new_pairs[rules[pair] + pair[1]] += pairs[pair]
        pairs = new_pairs


line_of_text_, pairs_, rules = get_data()
print(f"Part 1 answer is: {calculate_result(line_of_text_, pairs_, 10)}")
print(f"Part 1 answer is: {calculate_result(line_of_text_, pairs_, 40)}")
