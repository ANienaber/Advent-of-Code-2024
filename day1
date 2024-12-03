if __name__ == '__main__':
    file = open("day1.txt", "r")
    list1 = []
    list2 = []
    
    line = file.readline()
    while line:
        split_line = line.split()
        list1.append(split_line[0])
        list2.append(split_line[1])
        line = file.readline()
    file.close()

    #part1
    list1.sort()
    list2.sort()
    sum = 0
    for i in range(len(list1)):
        sum += abs(int(list1[i])-int(list2[i])) 
    print(sum)
    
    #part2
    similarity_score = 0
    j=0
    
    for i in range(len(list1)):
        sim = 0
        if i != 0 and int(list1[i]) == int(list1[i-1]):
            continue
        while j < len(list2) and int(list1[i]) > int(list2[j]):
            j += 1
        while j < len(list2) and int(list1[i]) == int(list2[j]):
            j+=1
            sim+=1
        if j >= len(list2):
            break
        similarity_score += int(list1[i]) * sim
        
    print(similarity_score)