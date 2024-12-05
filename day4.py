import re

if __name__ == '__main__':
    file = open("day4.txt", "r")

    lines = [line.strip() for line in file if line.strip()]

    occurrences = 0
    top_left_occurrences = 0
    top_middle_occurrences = 0
    top_right_occurrences = 0
    middle_right_occurrences = 0
    bottom_right_occurrences = 0
    bottom_middle_occurrences = 0
    bottom_left_occurrences = 0
    middle_left_occurrences = 0

    # for line in lines:
    #     horizontals = re.findall("XMAS", line)
    #     horizontal_occurrences += len(horizontals)
    #
    # for line in lines:
    #     backwards = re.findall("SAMX", line)
    #     backwards_occurrences += len(backwards)
    #
    # #vertical
    # for i in range(len(lines)):
    #     for j in range(len(lines[i])):
    #         if lines[i][j] == "X" and i+3 <= len(lines):
    #             if lines[i+1][j] == "M" and lines[i+2] == "A" and lines[i+3] == "S":
    #                 vertical_occurrences += 1

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "X":
                #top left
                if i >= 3 and j >= 3 and lines[i - 1][j - 1] == "M" and lines[i - 2][j - 2] == "A" and lines[i - 3][j - 3] == "S":
                    top_left_occurrences += 1
                #top middle
                if j >= 3 and lines[i][j - 1] == "M" and lines[i][j - 2] == "A" and lines[i][j - 3] == "S":
                    top_middle_occurrences += 1
                #top right
                if i+3 < len(lines) and j >= 3 and lines[i + 1][j - 1] == "M" and lines[i + 2][j - 2] == "A" and lines[i + 3][j - 3] == "S":
                    top_right_occurrences += 1
                #middle right
                if i + 3 < len(lines) and lines[i + 1][j] == "M" and lines[i + 2][j] == "A" and lines[i + 3][j] == "S":
                    middle_right_occurrences += 1
                #bottom right
                if i + 3 < len(lines) and j + 3 < len(lines[i]) and lines[i + 1][j + 1] == "M" and lines[i + 2][j + 2] == "A" and lines[i + 3][j + 3] == "S":
                    bottom_right_occurrences += 1
                #bottom middle
                if j + 3 < len(lines[i]) and lines[i][j + 1] == "M" and lines[i][j + 2] == "A" and lines[i][j + 3] == "S":
                    bottom_middle_occurrences += 1
                #bottom left
                if i >= 3 and j + 3 < len(lines) and lines[i - 1][j + 1] == "M" and lines[i - 2][j + 2] == "A" and lines[i - 3][j + 3] == "S":
                    bottom_left_occurrences += 1
                #middle left
                if i >= 3 and lines[i - 1][j] == "M" and lines[i - 2][j] == "A" and lines[i - 3][j] == "S":
                    middle_left_occurrences += 1

    print(top_left_occurrences + top_middle_occurrences + top_right_occurrences + middle_right_occurrences + bottom_right_occurrences + bottom_middle_occurrences + bottom_left_occurrences + middle_left_occurrences)
