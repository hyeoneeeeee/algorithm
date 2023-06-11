for _ in range(int(input())):
    n = int(input())
    if n == 0 or n == 1:
        print(2)
        continue
    while True:
        a = True
        for i in range(2,n//2+1):
            if n % i == 0:
                a = False
                break
        if a == True:
            print(n)
            break
        else:
            n += 1
