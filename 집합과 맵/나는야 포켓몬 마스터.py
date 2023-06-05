import sys
poketmonster_dic = {}
poketmonster_dic_reverse = {}
n,m = map(int, input().split())
for i in range(1,n+1):
    name = sys.stdin.readline().strip()
    poketmonster_dic[i] = name
    poketmonster_dic_reverse[name] = i
for _ in range(m):
    q = sys.stdin.readline().strip()
    if q.isdigit() == True:
        print(poketmonster_dic[int(q)])
    else:
        print(poketmonster_dic_reverse[q])