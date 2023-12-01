with open('day-1/input.txt') as f:
    inputLines = f.readlines()

result = 0

replace_map = {
    "one": "o1e", 
    "two": "t2o",
    "three": "t3e", 
    "four": "f4r", 
    "five": "f5e", 
    "six": "s6x", 
    "seven": "s7n", 
    "eight": "e8t", 
    "nine": "n9e"
}
def_list = []

for lines in inputLines:
    for word, digit in replace_map.items():
        lines = lines.replace(word, digit) 
    def_list.append(lines.strip())    

for line in def_list:
    print("base = ", line)

    chunks = ''.join(filter(str.isdigit, line)).split()

    for chunk in chunks:
        if len(chunk) == 1:
            chunk = chunk * 2
        elif len(chunk) > 2:
            chunk = chunk[0] + chunk[-1]

    print("num = ", chunk, "\n")
    result += int(chunk)

print(result)
