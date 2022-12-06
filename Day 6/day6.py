with open("input.txt", "r") as f:
    letters = [letter for letter in f.read()]
    for i in range(4, len(letters)):
        part = letters[i-4:i]
        if sorted(part) == sorted(list(set(part))):
            print("Part 1:  ", i)
            break
    for i in range(14, len(letters)):
        part = letters[i-14:i]
        if sorted(part) == sorted(list(set(part))):
            print("Part 2:  ", i)
            break