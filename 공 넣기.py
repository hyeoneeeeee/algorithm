
#  출력 초과 = print를 지우지 않고 제출
N, M = map(int, (input().split(" ")))
A = ["0" for _ in range(N)]
B = []
for x in range(M):
    a, b, c = map(int, input().split(" "))
    for y in range(a-1,b):
        A[y] = str(c)
print(" ".join(A))

