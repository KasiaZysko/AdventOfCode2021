from aocd.models import Puzzle


def get_data():
    puzzle = Puzzle(year=2021, day=8)
    dataset = puzzle.input_data
    dataset = dataset.split("\n")
    dataset_1 = [d.split("| ")[1] for d in dataset]
    dataset_1 = [d.split(" ") for d in dataset_1]
    dataset_2 = [d.split("| ") for d in dataset]
    return dataset_1, dataset_2


def part_1(data):
    counter = 0
    for new_data_line in data:
        for x in new_data_line:
            if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7:
                counter += 1
    return counter


def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key


def part_2(data):
    numbers_template = {0: "012456", 1: "25", 2: "02346", 3: "02356", 4: "1235", 5: "01356", 6: "013456", 7: "025",
                        8: "0123456", 9: "012356"}
    last_value = 0
    for new_data in data:
        number = ""
        alpha_occurrence = {}
        positions = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: ""}
        ten_numbers = new_data[0]
        for y in "abcdefg":
            alpha_occurrence[ten_numbers.count(y)] = y

        positions[4], positions[1], positions[5] = alpha_occurrence[4], alpha_occurrence[6], alpha_occurrence[9]
        ten_numbers = ten_numbers.split(" ")
        for x in ten_numbers:
            if len(x) == 2:
                positions[2] = x.replace(positions[5], "")
        for x in ten_numbers:
            if len(x) == 3:
                positions[0] = x.replace(positions[5], "").replace(positions[2], "")
        for x in ten_numbers:
            if len(x) == 4:
                positions[3] = x.replace(positions[1], "").replace(positions[2], "").replace(positions[5], "")
        positions[6] = [x for x in "abcdefg" if x not in list(positions.values())][0]
        new_data = new_data[1].split(" ")

        for x in new_data:
            string_number = ""
            for y in x:
                string_number += str(get_key(y, positions))
            string_number = "".join(sorted(string_number))
            number += str(get_key(string_number, numbers_template))
        last_value += int(number)
    return last_value


data_1, data_2 = get_data()
print(f"Part 1 answer is: {part_1(data_1)}")
print(f"Part 2 answer is: {part_2(data_2)}")
