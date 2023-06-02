n = input()
c1 = set(map(int, input().split()))
m = input()
c2 = list(map(int, input().split()))
for i in c2:
    if i in c1:
        print(1, end=" ")
    else:
        print(0, end=" ")