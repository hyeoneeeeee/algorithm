t=int(input())
n,x=1,1
while True:
    if t > n:
        t-=n
        n+=1
    else:
        if n==1:
            print("1/1"); break
        elif n%2 == 1:
            while True:
                if t == 1:
                    print(f"{n}/{x}"); break
                t-=1; n-=1; x+=1
            break
        else:
            while True:
                if t == 1:
                    print(f"{x}/{n}"); break
                t-=1; n-=1; x+=1
            break