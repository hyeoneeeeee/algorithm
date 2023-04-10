n,m = map(int, input().split(" "))
a = [str(x) for x in range(n+1)]
for _ in range(m):
    num1, num2 = map(int, input().split(" "))
    a[num1], a[num2] = a[num2], a[num1]
print(*a[1:])