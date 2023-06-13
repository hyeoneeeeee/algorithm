import sys
def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

for _ in range(int(sys.stdin.readline().strip())):
    n = int(sys.stdin.readline().strip())
    if n == 0 or n == 1:
        print(2)
        continue
    while True:
        if is_prime(n):
            print(n)
            break
        else:
            n += 1
