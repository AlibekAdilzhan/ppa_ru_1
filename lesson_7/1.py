a = [
    [1, 2, 3, 4],
    [0, -1, 99, 1],
    [-1, 1, 1, 2],
    [1, -1, 1000, 3]
]

s = 0

for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=" ")
    print()
    