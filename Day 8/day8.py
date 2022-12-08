with open("input.txt", "r") as f:
    counterA = 0
    scenicScores = []
    map = f.read().splitlines()
    for y in range(1, len(map) - 1):
        for x in range(1, len(map[y]) - 1):
            notVisible = False
            tree = int(map[y][x])
            for other in range(x):
                if int(map[y][other]) >= tree:
                    break
            else:
                notVisible = True
            for other in range(y):
                if int(map[other][x]) >= tree:
                    break
            else:
                notVisible = True
            for other in range(x + 1, len(map[y])):
                if int(map[y][other]) >= tree:
                    break
            else:
                notVisible = True
            for other in range(y + 1, len(map)):
                if int(map[other][x]) >= tree:
                    break
            else:
                notVisible = True
            if notVisible:
                counterA += 1

    print("Part 1:  ", counterA + 2 * len(map) + 2 * (len(map[0]) - 2))

    for y in range(len(map)):
        for x in range(len(map[y])):
            tree = int(map[y][x])
            scenic = [0, 0, 0, 0]
            for left in range(1, x + 1):
                if x == left or int(map[y][x-left]) >= tree:
                    scenic[0] = left
                    break
            for right in range(1, len(map[y]) - x):
                if x + right + 1 == len(map[y]) or int(map[y][x+right]) >= tree:
                    scenic[1] = right
                    break
            for up in range(1, y + 1):
                if y == up or int(map[y-up][x]) >= tree:
                    scenic[2] = up
                    break
            for down in range(1, len(map) - y):
                if y + down + 1 == len(map) or int(map[y+down][x]) >= tree:
                    scenic[3] = down
                    break
            scenicScores.append(scenic[0] * scenic[1] * scenic[2] * scenic[3])

    print("Part 2:  ", max(scenicScores))