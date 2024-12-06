from multiprocessing import Pool
from tqdm import tqdm

obstacles = set()
f = open("inputs/6.txt").read().split()
height, width = len(f), len(f[0]) - 1

for y, line in enumerate(f):
    for x, char in enumerate(line):
        if char == "#":
            obstacles.add((y, x))
        elif char == "^":
            start_guard = (y, x)

def is_loop(y, x):
    guard = start_guard
    turns = set() # store guard state i.e. pos and direction
    direction = (-1, 0)

    while 0 <= guard[0] < height and 0 <= guard[1] < width:
        new_guard = (guard[0] + direction[0], guard[1] + direction[1])

        if new_guard in obstacles or new_guard == (y, x):
            direction = (direction[1], -direction[0])
            state = (guard, direction)
            if state in turns:
                return 1
            else:
                turns.add(state)
        else:
            guard = new_guard

    return 0

with Pool() as p:
    positions = [(y, x) for y in range(height) for x in range(width)]
    part_b = sum(p.starmap(is_loop, positions))

print("Part B:", part_b)