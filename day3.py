import re

if __name__ == '__main__':
    file = open("day3.txt", "r")

    # #part1
    # lines = [line.strip() for line in file if line.strip()]
    # nums = []
    # mul_sum = 0
    # for line in lines:
    #     ops = re.findall("mul\\([0-9]+,[0-9]+\\)", line)
    #     print(ops)
    #     for op in ops:
    #         nums.append(re.findall("[0-9]+", op))
    # print(nums)
    # for i in range(0, len(nums)):
    #     mul_sum += int(nums[i][0]) * int(nums[i][1])
    # print(mul_sum)

    # part2
    lines = [line.strip() for line in file if line.strip()]
    nums = []
    mul_sum = 0
    all_lines = ""
    for line in lines:
        all_lines += line
    print(all_lines)
    all_lines += "do()"
    ops = re.sub("don't\\(\\).+?do\\(\\)", "", all_lines)
    print(ops)
    ops = re.findall("mul\\([0-9]+,[0-9]+\\)", ops)
    print(ops)
    for op in ops:
        nums.append(re.findall("[0-9]+", op))
    print(nums)
    for i in range(0, len(nums)):
        mul_sum += int(nums[i][0]) * int(nums[i][1])
    print(mul_sum)

