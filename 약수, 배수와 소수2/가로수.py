import sys
from math import gcd
n = int(input())
arr = [int(sys.stdin.readline().strip()) for _ in range(n)]
dist = [arr[i+1]-arr[i] for i in range(n-1)]
print(((max(arr)-min(arr))//(gcd(*dist)))-n+1)