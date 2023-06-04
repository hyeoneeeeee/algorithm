n = int(input())
dic = {}
for _ in range(n):
    name, status = map(str, input().split())
    dic[f"{name}"] = status
name_list = [x for x in dic if dic[f"{x}"]=="enter"]
name_list = sorted(name_list, reverse=True)
for x in name_list:
    print(x)