a, b = input(), input()
len_a, len_b = len(a), len(b)

a = (len_b-len_a)*"0"+a if len_a < len_b else a
b = (len_a-len_b)*"0"+b if len_b < len_a else b

resp_a = ""
resp_b = ""


for i in range(len(a)-1, -1, -1):
    if int(a[i]) < int(b[i]):
        resp_b = b[i] + resp_b
    elif int(a[i]) > int(b[i]):
        resp_a = a[i] + resp_a
    else:
        resp_b = b[i] + resp_b
        resp_a = a[i] + resp_a

print(*sorted([int(resp_a if resp_a != "" else -1), int(resp_b if resp_b != "" else -1)]))