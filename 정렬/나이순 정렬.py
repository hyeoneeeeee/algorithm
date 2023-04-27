import sys
l=[]
n=int(sys.stdin.readline())
for i in range(n):
    y,name = map(str, sys.stdin.readline().split())
    l.append([int(y),name])
l.sort(key= lambda x: x[0])
for j in range(n):
    print(f"{l[j][0]} {l[j][1]}")