from aocd.models import Puzzle
import math

puzzle = Puzzle(year=2021, day=17)
data = puzzle.input_data


def sgn(x):
    return (x > 0) - (x < 0)


def simulate(vx, vy, target, step=600):
    x = y = 0
    max_y = 0
    x0, xn, y0, yn = target
    if (vx > 0 and xn < x) or (vx <= 0 and x0 > x) or (vy <= 0 and y0 > y):
        return -1
    for step in range(step):
        x += vx
        y += vy
        max_y = max(y, max_y)

        if x0 <= x <= xn and y0 <= y <= yn:
            return max_y

        vx -= sgn(vx)
        vy -= 1
    return -1


x_target = data.split()[2].replace("x=", "").replace(",", "").split("..")
x_target = [int(x) for x in x_target]
y_target = data.split()[3].replace("y=", "").replace(",", "").split("..")
y_target = [int(y) for y in y_target]

target = (min(x_target), max(x_target), min(y_target), max(y_target))

min_x_vel = int(math.sqrt(target[0]))
max_x_vel = target[1] + 1
min_y_vel = target[2]
max_y_vel = abs(target[2]) + 1
print(target)
max_y = 0
viable = 0

for vx in range(min_x_vel, max_x_vel):
    for vy in range(min_y_vel, max_y_vel):
        sim = simulate(vx, vy, target)
        max_y = max(max_y, sim)
        viable += sim >= 0

print("max y", max_y)
print("number of viable initial velocities", viable)

mi = -min_y_vel - 1
print(mi*(mi+1)/2)