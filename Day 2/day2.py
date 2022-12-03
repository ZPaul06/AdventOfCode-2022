def valueOf(key):
    if key == "A" or key == "X":
        return 1
    if key == "B" or key == "Y":
        return 2
    if key == "C" or key == "Z":
        return 3

with open("input.txt", "r") as f:
    score = 0
    for line in f.read().splitlines():
        challenge = line.split(" ")
        me = valueOf(challenge[1])
        opponent = valueOf(challenge[0])
        if me == opponent:
            score += me + 3
        elif opponent - (me % 3) == 1:
            score += me
        elif me - (opponent % 3) == 1:
            score += me + 6

    print("Part 1:  ", score)

with open("input.txt", "r") as f:
    score = 0
    for line in f.read().splitlines():
        challenge = line.split(" ")
        hint = challenge[1]
        opponent = valueOf(challenge[0])
        if hint == "X":
            me = opponent + 2 if opponent - 1 == 0 else opponent - 1
            score += me
        elif hint == "Y":
            score += opponent + 3
        elif hint == "Z":
            me = opponent - 2 if opponent + 1 == 4 else opponent + 1
            score += me + 6
        
    print("Part 2:  ", score)
