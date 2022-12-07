def deepSum(tree):
    if type(tree) == list:
        return sum(deepSum(branch) for branch in tree)
    else:
        return int(tree)


def atMost100000(tree):
    if type(tree) == list:
        total = deepSum(tree) if deepSum(tree) <= 100000 else 0
        for branch in tree:
            total += atMost100000(branch)
        return total
    else:
        return 0


def findToClear(tree, toBeCleared, clearable):
    if type(tree) == list:
        if deepSum(tree) >= toBeCleared:
            clearable.append(deepSum(tree))
        for branch in tree:
            findToClear(branch, toBeCleared, clearable)
    return clearable


    
with open("input.txt", "r") as f:
    commands = f.read().split("\n$ ")
    levels = {"/": [[]]}
    tree = []
    currentPath = []
    for command in commands:
        if command.startswith("cd"):
            if command[3:] == "/":
                currentPath = []
            elif command[3:] == "..":
                currentPath = currentPath[:len(currentPath)-1]
            else:
                for path in levels[command[3:]]:
                    if path[:len(path)-1] == currentPath:
                        currentPath = path
                        break
        elif command.startswith("ls"):
            output = command.split("\n")[1:]
            for line in output:
                node = tree
                for i in range(len(currentPath)):
                    node = node[currentPath[i]]
                if line.startswith("dir"):
                    if line[4:] in levels:
                        levels[line[4:]].append(currentPath + [len(node)])
                    else:
                        levels.update({line[4:]: [currentPath + [len(node)]]})
                    node.append([])
                else:
                    node.append(line.split(" ")[0])

    print("Part 1:  ", atMost100000(tree))

    toBeCleared = 30000000 - (70000000 - deepSum(tree))

    print("Part 2:  ", min(findToClear(tree, toBeCleared, [])))
                    