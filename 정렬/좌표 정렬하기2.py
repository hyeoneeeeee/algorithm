import sys
l=[]
n=int(input())
for _ in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))
l.sort(key= lambda x: (x[1], x[0]))
for i in range(n):
    print(*l[i])