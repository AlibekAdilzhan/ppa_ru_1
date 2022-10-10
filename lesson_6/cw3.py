l1 = ["Kazakhstan", "Russia", "China", "S Korea", "KKK"]
l2 = ["Astana", "Moscow", "Pekin", "Seol"]

d1 = {1 : "a", 2 : "b", 3 : "c"}
d2 = dict(zip(l1, l2))
print(d1)
print(d2)
# d = dict([(1, "a"), (2, "b"), (3, "c")])
# print(dict(l1, l2))
print(dict(zip(d1, d2)))
# print(d)