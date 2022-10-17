import random

a = random.randint(1, 100)
n = 10
# random_list = [random.randint(1, 100) for i in range(n)]
r2d = []
for j in range(n):
    random_list = []
    for i in range(n):
        a = random.randint(1, 100)
        random_list.append(a)
    r2d.append(random_list)

for x in r2d:
    print(x)