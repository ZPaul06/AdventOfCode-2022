with open("input.txt", "r") as f:
    content = f.read().split("\n\n")
    store, instructions = list(reversed(content[0].split("\n"))), content[1]
    stacks = [[] for i in store[0].split("  ")]
    for row in store[1:]:
        for i in range(len(stacks)):
            if (item := row[1 + i + (i * 3)]) != " ":
                stacks[i].append(item)
    for row in instructions.split("\n"):
        row = row.replace("move ", "")
        row = row.replace("from", "")
        row = row.replace("to", "")
        howMany, fromStack, toStack = int(row.split("  ")[0]), int(row.split("  ")[1]), int(row.split("  ")[2])
        for i in range(howMany):
            stacks[toStack - 1].append(stacks[fromStack - 1].pop())
    print("Part 1:  ", "".join(stack[len(stack) - 1] for stack in stacks))
    
    stacks = [[] for i in store[0].split("  ")]
    for row in store[1:]:
        for i in range(len(stacks)):
            if (item := row[1 + i + (i * 3)]) != " ":
                stacks[i].append(item)
    for row in instructions.split("\n"):
        row = row.replace("move ", "")
        row = row.replace("from", "")
        row = row.replace("to", "")
        howMany, fromStack, toStack = int(row.split("  ")[0]), int(row.split("  ")[1]), int(row.split("  ")[2])
        copy = [stacks[fromStack - 1].pop() for i in range(howMany)]
        for item in list(reversed(copy)):
            stacks[toStack - 1].append(item)
    print("Part 2:  ", "".join(stack[len(stack) - 1] for stack in stacks))