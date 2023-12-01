with open('day-1/input.txt') as f:
    inputLines = f.readlines()

result = 0

for line in inputLines:
    line = ''.join(filter(str.isdigit, line))
    print("line = ", line)

    if len(line) == 1:
        line = line * 2
    elif len(line) > 2:
        line = line[0] + line[-1]

    print("num = ", line, "\n")
    result += int(line)

print(result)
