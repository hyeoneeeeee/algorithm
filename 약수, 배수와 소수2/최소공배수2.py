import sys
A,B=map(int, sys.stdin.readline().strip().split())
a,b=A,B
while b != 0:
    a = a%b
    a,b=b,a
print(int(A*B/a))