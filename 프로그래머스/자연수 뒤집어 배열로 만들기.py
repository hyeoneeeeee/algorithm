# 처음에 푼것
def solution(n):
    return list(reversed(list(map(int,str(n)))))

# 고친것
def solution(n):
    return list(map(int,reversed(str(n))))

# reverse = 뒤집기만 하고 return 값 null
# reversed = 뒤집고 뒤집은 값 객체로 return
# reverse 대신 [::-1] 가능