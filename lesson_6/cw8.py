with open("1.txt", "r") as fo:
    lines = fo.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

for i in range(len(lines)):
    print(lines[i])