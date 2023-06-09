import sys
A,B = map(int, sys.stdin.readline().strip().split())
C,D = map(int, sys.stdin.readline().strip().split())
N,M = (A*D)+(C*B),B*D; n,m = N,M
while n != 0:
    m = m%n
    n,m = m,n
print(f"{int(N/m)} {int(M/m)}")