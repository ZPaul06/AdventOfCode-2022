with open("input.txt", "r") as f:
    fullyContains, overlaps = 0, 0
    for line in f.read().splitlines():
        startA, endA, startB, endB = int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]), int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1])
        if (startA >= startB and endA <= endB) or (startB >= startA and endB <= endA): fullyContains += 1
        if (startB <= startA <= endB) or (startB <= endA <= endB) or (startA <= startB <= endA) or (startA <= endB <= endA): overlaps += 1
        
    print("Part 1:  ", fullyContains)
    print("Part 2:  ", overlaps)