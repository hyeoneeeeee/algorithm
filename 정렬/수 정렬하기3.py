import sys
n=int(input())
l=[0]*10001
for _ in range(n):
    l[int(sys.stdin.readline())] +=1
for x in range(10001):
    if l[x] !=0:
        for y in range(l[x]):
            print(x)