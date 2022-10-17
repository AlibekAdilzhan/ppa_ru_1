n = 10

a = [[0] * n for i in range(10)]

a[2][3] = 99

for i in range(len(a)):
    print(a[i])