# join 사용
def solution(n):
    sum = 0
    for a in ','.join([str(n)]):
        sum += int(a)
    return sum

# map사용
def solution(n):
    return sum(map(int,str(n)))
