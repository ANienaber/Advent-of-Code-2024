def check_level(le):
    s = True
    inc = le[0] < le[1]
    for k in range(1, len(le)):
        if (not inc and le[k - 1] < le[k]) or (inc and le[k - 1] > le[k]):
            s = False
        if abs(le[k - 1] - le[k]) > 3 or abs(le[k - 1] - le[k]) == 0:
            s = False
    return s


if __name__ == '__main__':
    file = open("day2.txt", "r")

    lines = [line.strip() for line in file if line.strip()]
    reports = []
    for line in lines:
        reports.append(list(map(int, line.split())))
        
    # part1
    safe_reports = 0
    for levels in reports:
        safe = True
        increase = levels[0] < levels[1]
        for i in range(1, len(levels)):
            if (not increase and levels[i - 1] < levels[i]) or (increase and levels[i - 1] > levels[i]):
                safe = False
            if abs(levels[i - 1] - levels[i]) > 3 or abs(levels[i - 1] - levels[i]) == 0:
                safe = False
        if safe:
            safe_reports += 1
    print(safe_reports)

    #part2
    safe_reports = 0
    ids = []
    for j in range(0, len(reports)):
        levels = reports[j]
        safe = True
        joker = True
        alt = None
        i = 1
        while i < len(levels):
            increase = levels[0] < levels[1]
            if (not increase and levels[i - 1] < levels[i]) or (increase and levels[i - 1] > levels[i]) or abs(
                    levels[i - 1] - levels[i]) > 3 or abs(levels[i - 1] - levels[i]) == 0:
                if joker:
                    found_alt = False
                    for k in range(0, len(levels)):
                        test = levels.copy()
                        test.remove(levels[k])
                        if check_level(test):
                            levels.pop(k)
                            found_alt = True
                            break
                    if not found_alt:
                        safe = False
                    joker = False
                else:
                    safe = False
            i += 1
        if safe:
            safe_reports += 1
    print(safe_reports)