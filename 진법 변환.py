n, b = input().split()
n = ''.join(reversed(n))
bit = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0
for i in range(len(n)):
    num = bit.index(n[i])
    result += num*int(b)**i
print(result)