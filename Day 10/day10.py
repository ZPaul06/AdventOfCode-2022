with open("input.txt", "r") as f:
    instructions = f.read().splitlines()
    register, cycleCounter = 1, 0
    signalStrengthSum = 0
    screen = ["" for i in range(6)]
    litPixel, darkPixel = "#", "."
    for instruction in instructions:
        cycleCounter += 1
        if cycleCounter % 40 == 20:
            signalStrengthSum += cycleCounter * register
        if (cycleCounter % 40) - 1 in range(register-1,register+2):
            screen[int((cycleCounter-1)/40)] += litPixel
        else:
            screen[int((cycleCounter-1)/40)] += darkPixel
        if instruction.startswith("addx"):
            cycleCounter += 1
            if cycleCounter % 40 == 20:
                signalStrengthSum += cycleCounter * register
            if (cycleCounter % 40) - 1 in range(register-1,register+2):
                screen[int((cycleCounter-1)/40)] += litPixel
            else:
                screen[int((cycleCounter-1)/40)] += darkPixel
            register += int(instruction[5:])

    print("Part 1:  ", signalStrengthSum)
    
    print("Part 2:")
    for row in screen: print(row)