import sys
prime_list = []
def get_prime(x):
    for num in range(2, 2*x+1):
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                break
        else:
            prime_list.append(num)
get_prime(123456)
while True:
    c=0
    n=int(sys.stdin.readline().strip())
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        for i in prime_list:
            if n < i <= 2*n:
                c += 1
        print(c)