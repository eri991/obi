s, a, b = int(input()), int(input()), int(input())
count = 0
for i in range(a,b+1):
    count += 1 if sum([int(x) for x in list(str(i))]) == s else 0

print(count)