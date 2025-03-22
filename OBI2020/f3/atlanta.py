a = int(input())
b = int(input())
resp = [-1, -1]
for i in range(1, int(round((a+b)**(1/2),1))+1):
    x = i
    y = int((a+b)/x)
    if x*y == a+b and x+y == (a+4)/2:
        resp = sorted([x,y])
        break

print(" ".join([str(i) for i in resp]))