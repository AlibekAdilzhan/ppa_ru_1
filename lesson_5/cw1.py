#    01234567
a = "abcdecfg" # len(a) = 8
t = "c"
c = []
for i in range(len(a)):
    if a[i] == t:
        c.append(i)

print(c)