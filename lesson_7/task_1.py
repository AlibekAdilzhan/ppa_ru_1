n, m = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for i in range(n)]

maxi = -100000000000000
index_i, index_j = 0, 0

for i in range(n):
    for j in range(m):
        if a[i][j] > maxi:
            index_i = i
            index_j = j
            maxi = a[i][j]
            
print(index_i, index_j)
