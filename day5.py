import re

if __name__ == '__main__':
    file = open("day5.txt", "r")

    lines = [re.sub("\\n", "", line) for line in file]

    #part1
    sum = 0
    rules = []
    updates = []
    rules_done = False
    i = 0
    while i < len(lines):
        while lines[i] != "" and not rules_done:
            rules.append(re.split("\\|", lines[i]))
            i += 1
        rules_done = True
        if lines[i] == "":
            i+=1
            continue
        updates.append(re.split(",", lines[i]))
        i+=1

    incorrect_updates = []
    for update in updates:
        right_order = True
        for i in range(1, len(update)):
            for rule in rules:
                if update[i] == rule[0]:
                    for j in range(i-1, -1, -1):
                        if update[j] == rule[1]:
                            right_order = False
                            incorrect_updates.append(update)
                            break
                if not right_order:
                    break
            if not right_order:
                break

        if right_order:
            middle_number = int(update[int((len(update))/2)])
            #print(middle_number)
            sum += middle_number

    print(sum)

    #part2
    sum2  = 0
    for update in incorrect_updates:
        i = 1
        while i < len(update):
            for rule in rules:
                if update[i] == rule[0]:
                    for j in range(i-1, -1, -1):
                        if update[j] == rule[1]:
                            update.insert(j, update[i])
                            update.pop(i+1)
                            i = 1
            i += 1
        print(update)

    for update in incorrect_updates:
        middle_number = int(update[int((len(update)) / 2)])
        #print(middle_number)
        sum2 += middle_number

    print(sum2)
