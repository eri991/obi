a, b = list(map(int, input().split()))
sa, sb = input().split(), input().split()

for i in range(len(sa)):
    count = 0
    if sa[i] == sb[count]:
        sb.remove(sb[count])
        count += 1

print("N") if sb else print("S")