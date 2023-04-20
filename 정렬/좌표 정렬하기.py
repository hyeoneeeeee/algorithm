import sys
l=[]
n=int(input())
for _ in range(n):
    x,y=map(int,sys.stdin.readline.split())
    l.append([x,y])
l.sort(key=lambda x: (x[0],x[1]))
for i in range(n):
    print(*l[i])