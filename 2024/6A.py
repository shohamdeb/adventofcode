obstacles = set()
f = open("inputs/6.txt").read().split()
height, width = len(f), len(f[0]) - 1

for y, line in enumerate(f):
    for x, char in enumerate(line):
        if char == "#":
            obstacles.add((y, x))
        elif char == "^":
            guard = (y, x)

visited = set()
direction = (-1, 0)

while 0 <= guard[0] < height and 0 <= guard[1] < width:
    visited.add(guard)
    new_guard = (guard[0] + direction[0], guard[1] + direction[1])

    if new_guard in obstacles or new_guard == (y, x):
        direction = (direction[1], -direction[0])
        state = (guard, direction)
    else:
        guard = new_guard

print("Part A:", len(visited))