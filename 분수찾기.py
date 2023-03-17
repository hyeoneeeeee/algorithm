t=int(input())
n,x,y=1,0,0
while True:
    if t > n:
        t-=n
        n+=1
    elif t <= n:
        if t%2 == 1:
            