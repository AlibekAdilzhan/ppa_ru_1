n = 10

a = [[0 for i in range(n)] for j in range(n)]

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             a[i][j] = 1

for j in range(n):
    a[j][j] = 1

for i in range(len(a)):
    print(a[i])