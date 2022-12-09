def moveUp(head, tail):
    if (head[0] == tail[0] and abs(head[1] - tail[1]) == 1) or (head[1] == tail[1] and abs(head[0] - tail[0]) == 1):
        return
    if head[0] == tail[0] and abs(head[1] - tail[1]) != 1:
        tail[1] = int((head[1] + tail[1]) / 2)
    elif head[1] == tail[1] and abs(head[0] - tail[0]) != 1:
        tail[0] = int((head[0] + tail[0]) / 2)
    elif abs(head[0] - tail[0]) != 1 and abs(head[1] - tail[1]) != 1:
        tail[0] = int((head[0] + tail[0]) / 2)
        tail[1] = int((head[1] + tail[1]) / 2)
    elif abs(head[0] - tail[0]) != 1:
        tail[0] = int((head[0] + tail[0]) / 2)
        tail[1] = head[1]
    elif abs(head[1] - tail[1]) != 1:
        tail[0] = head[0]
        tail[1] = int((head[1] + tail[1]) / 2)
        


with open("input.txt", "r") as f:
    motionSeries = f.read().splitlines()
    head = [0,0]
    tail = [0,0]
    visitedByTail = []
    for motion in motionSeries:
        direction = motion[0]
        for i in range(int(motion[2:])):
            if direction == "R":
                head[0] += 1
            elif direction == "D":
                head[1] -= 1
            elif direction == "L":
                head[0] -= 1
            elif direction == "U":
                head[1] += 1
            moveUp(head, tail)
            visitedByTail.append(str(tail))

    print("Part 1:  ", len(set(visitedByTail)))

    knots = [[0,0] for i in range(10)]
    visitedByLastKnot = []
    for motion in motionSeries:
        direction = motion[0]
        for i in range(int(motion[2:])):
            if direction == "R":
                knots[0][0] += 1
            elif direction == "D":
                knots[0][1] -= 1
            elif direction == "L":
                knots[0][0] -= 1
            elif direction == "U":
                knots[0][1] += 1
            for i in range(9):
                moveUp(knots[i], knots[i+1])
            visitedByLastKnot.append(str(knots[9]))

    print("Part 2:  ", len(set(visitedByLastKnot)))
            
