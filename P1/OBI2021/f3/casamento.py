a, b = input(), input()
while len(a) < len(b):
    a = "0" + a
a, b = list(a), list(b)
for index in range(len(a)):
    if int(a[index]) < int(b[index]):
        a[index] = ""
    elif int(b[index]) < int(a[index]):
        b[index] = ""
a, b = "".join([i for i in a]), "".join([i for i in b])
print(" ".join(str(int(i)) for i in sorted([a if a else "-1", b if b else "-1"])))