with open("input.txt", "r") as f:
    allElves = []
    currentElf = 0
    for line in f.read().splitlines():
        if line == "":
            allElves.append(currentElf)
            currentElf = 0
        else:
            currentElf += int(line)

    print("Part 1:  ", max(allElves))

    top3 = 0
    for i in range(3):
        newMax = max(allElves)
        top3 += newMax
        allElves.remove(newMax)

    print("Part 2:  ", top3)
