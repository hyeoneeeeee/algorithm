n, b = map(int,input().split())
l = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = ''
while n!=0:
    a += l[n%b]
    n = n//b
print(a[::-1])