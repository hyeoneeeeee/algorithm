import sys
l=[]
n=int(input())
for i in range(n):
    y,name = map(str, sys.stdin.readline().split())
    l.append([i,y,name])
l.sort(key= lambda x:(x[1], x[0]))
for j in range(n):
    print(f"{l[j][1]} {l[j][2]}")