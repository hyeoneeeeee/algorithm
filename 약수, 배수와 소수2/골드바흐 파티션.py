import sys
prime_list = [False, False] + [True]*999999
for i in range(2, 1000001):
    if prime_list[i]:
        for j in range(i*2, 1000001, i):
            prime_list[j] = False

for _ in range(int(input())):
    x = int(sys.stdin.readline().strip())
    count = 0
    for y in range(2,x//2+1):
        if prime_list[y] == True and prime_list[x-y] == True:
            count += 1
    else:
        print(count)
        count = 0