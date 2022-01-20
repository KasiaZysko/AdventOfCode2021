from aocd.models import Puzzle


def get_data():
    puzzle = Puzzle(year=2021, day=3)
    data = puzzle.input_data
    data_split = [line for line in data.split()]
    return data_split


def part1():
    oxygen_generator, epsilon_rate, gamma_rate = "", "", ""
    for x in range(0, len(numbers[0])):
        number0 = [number[x] for number in numbers]
        count_0 = number0.count("0")
        count_1 = number0.count("1")
        if count_1 > count_0:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"
    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def calculate_0_1(value_1, value_2):
    numbers_oxygen = get_data()
    for x in range(0, len(numbers[0])):
        number0 =[number[x] for number in numbers_oxygen]
        count_0 = number0.count("0")
        count_1 = number0.count("1")
        if count_0 > count_1:
            act_number = value_1
        else:
            act_number = value_2
        if value_1 == "0":
            numbers_oxygen = [number for number in numbers_oxygen if number[x] == act_number]
        else:
            if len(numbers_oxygen) != 1:
                numbers_oxygen = [number for number in numbers_oxygen if number[x] == act_number]
    return int(numbers_oxygen[0], 2)


def part2():
    no1 = calculate_0_1("0", "1")
    no2 = calculate_0_1("1", "0")
    return no1 * no2


numbers = get_data()
print(f"Part 1 answer is: {part1()}")
print(f"Part 2 answer is: {part2()}")
