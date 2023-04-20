import sys
n=int(input())
l=[]
for _ in range(n):
    l.append(int(sys.stdin.readline()))
l.sort()
for x in range(n):
    print(l[x])