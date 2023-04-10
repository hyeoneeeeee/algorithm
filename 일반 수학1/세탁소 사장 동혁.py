n = int(input())
p=[25,10,5,1]
for _ in range(n):
    num = int(input())
    while True:
        for i in p:
            print(num//i,end=' ')
            num = num%i
        else:
            break