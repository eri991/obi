h, p, f, d = list(map(int, input().split()))
while f != 16:
    f += d
    f = 15 if f == -1 else f
    if f == p:
        print("N")
        break
    elif f == h:
        print("S")
        break