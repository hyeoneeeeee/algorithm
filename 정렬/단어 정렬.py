l=[]
n=int(input())
for _ in range(n):
    l.append(input())
l=list(set(l))
l.sort(key= lambda x: (len(x), x))
for x in range(len(l)):
    print("".join(l[x]))