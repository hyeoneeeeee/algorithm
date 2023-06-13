import sys
def get_prime(x):
    for num in range(x+1, 2*x+1):
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                break
        else:
            prime_list.append(num)

while True:
    n=int(sys.stdin.readline().strip())
    prime_list = []
    if n == 0:
        break
    elif n == 1:
        print(1)
    else:
        get_prime(n)
        print(len(prime_list))
