#    012345 s[2] = c
s = "abcdbe"
t = "b"
x = "B"
new_s = ""
counter = 0
for i in range(len(s)):
    if counter == 0 and s[i] == "b":
        new_s = new_s + "B"
        counter += 1
    else:
        new_s = new_s + s[i]

print(new_s)