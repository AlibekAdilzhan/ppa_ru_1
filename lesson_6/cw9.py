# lines = ["Almaty", "Astana", "Seol", "Tokyo", "Toronto"]
lines = [1, 2, 3, 5]


with open("2.txt", "a") as fo:
    for i in range(len(lines)):
        fo.write(str(lines[i]) + "\n")