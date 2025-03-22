a = int(input())
b = int(input())
count = 0
for i in range(a, b+1):
    if i**(1/2) == int(i**(1/2)) and round(i**(1/3),2) == int(round(i**(1/3),2)):
        count += 1

print(count)