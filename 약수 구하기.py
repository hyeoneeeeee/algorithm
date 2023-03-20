a,b=map(int, input().split())
c=0; i=0
while True:
    i+=1
    if a%i==0:
        c+=1
        if c==b:
            print(i); break
    elif i>a:
        print(0); break
