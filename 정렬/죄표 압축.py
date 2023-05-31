n = int(input())
l = list(map(int, input().split()))
sl = sorted(list(set(l)))
dic = {sl[i] : i for i in range(len(sl))}
for x in l:
    print(dic[x], end=' ')