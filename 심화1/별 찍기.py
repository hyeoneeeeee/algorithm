# 왜 오답쓰..? (출력형식 오답)
a=int(input())
# for x in range(a+1): == 오답이유... 0부터 시작해서 오류
for x in range(1,a+1):
    print(" "*(a-x)+"*"*((2*x)-1))
for y in range(a-1,0,-1):
    print(" "*(a-y)+"*"*((2*y)-1))