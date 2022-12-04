def getPriority(c):
    return ord(c) - 38 if c.lower() != c else ord(c) - 96
    

with open("input.txt", "r") as f:
    prioritySum = 0
    for line in f.read().splitlines():
        partA = line[0:int(len(line)/2)]
        partB = line[int(len(line)/2):int(len(line))]
        sameItems = [c for c in partA if c in partB]
        prioritySum += sum(getPriority(c) for c in set(sameItems))

    print("Part 1:  ", prioritySum)

with open("input.txt", "r") as f:
    prioritySum = 0
    lines = f.read().splitlines()
    for i in range(int(len(lines)/3)):
        bagA, bagB, bagC = lines[3*i], lines[3*i+1], lines[3*i+2]
        sameItems = [c for c in bagA if c in bagB and c in bagC]
        prioritySum += sum(getPriority(c) for c in set(sameItems))

    print("Part 2:  ", prioritySum)