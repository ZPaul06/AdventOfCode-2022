def getPriority(c):
    if c.lower() != c:
        return ord(c) - 38
    else:
        return ord(c) - 96
    

with open("input.txt", "r") as f:
    prioritySum = 0
    for line in f.read().splitlines():
        partA = line[0:int(len(line)/2)]
        partB = line[int(len(line)/2):int(len(line))]
        sameItems = []
        for c in partA:
            if c in partB:
                sameItems.append(c)
        for c in set(sameItems):
            prioritySum += getPriority(c)

    print("Part 1:  ", prioritySum)

with open("input.txt", "r") as f:
    prioritySum = 0
    lines = f.read().splitlines()
    for i in range(int(len(lines)/3)):
        bagA = lines[3*i]
        bagB = lines[3*i+1]
        bagC = lines[3*i+2]
        sameItems = []
        for c in bagA:
            if c in bagB and c in bagC:
                sameItems.append(c)
        for c in set(sameItems):
            prioritySum += getPriority(c)

    print("Part 2:  ", prioritySum)
                
