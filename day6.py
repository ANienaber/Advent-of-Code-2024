import re
from enum import Enum


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


def find_start(li: list[list[str]]) -> list[int]:
    s = []
    for i1 in range(len(li)):
        if "^" in li[i1]:
            i2 = li[i1].index("^")
            s = [i1, i2]
    return s


if __name__ == '__main__':
    file = open("day6.txt", "r")

    lines = (re.sub("\n", "", line) for line in file)

    map_guard = []
    for line in lines:
        map_guard.append(list(line))
    print(map_guard)
    visited = set()
    start = find_start(map_guard)

    i = start[0]
    j = start[1]
    map_guard[i][j] = "."
    visited.add((i,j))
    current_direction = Direction.NORTH
    while 0 < i < len(map_guard)-1 and 0 < j < len(map_guard[i])-1:
        match current_direction:
            case Direction.NORTH:
                while i > 0:
                    if map_guard[i-1][j] == ".":
                        visited.add((i-1, j))
                    elif map_guard[i-1][j] == "#":
                        current_direction = Direction.EAST
                        break
                    i -= 1
            case Direction.EAST:
                while j < len(map_guard[i])-1:
                    if map_guard[i][j+1] == ".":
                        visited.add((i, j+1))
                    elif map_guard[i][j+1] == "#":
                        current_direction = Direction.SOUTH
                        break
                    j += 1
            case Direction.SOUTH:
                while i < len(map_guard)-1:
                    if map_guard[i+1][j] == ".":
                        visited.add((i+1, j))
                    elif map_guard[i+1][j] == "#":
                        current_direction = Direction.WEST
                        break
                    i += 1
            case Direction.WEST:
                while j > 0:
                    if map_guard[i][j-1] == ".":
                        visited.add((i, j-1))
                    elif map_guard[i][j-1] == "#":
                        current_direction = Direction.NORTH
                        break
                    j -= 1
    print(len(visited))
