g=[[0 for _ in range(101)]for _ in range(101)]
t=0
n=int(input())
for _ in range(n):
    x,y=map(int, input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            g[i][j]=1
for l in g:
    t+=sum(l)
print(t)
