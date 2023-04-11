x=[]
y=[]
for _ in range(int(input())):
    w,z=map(int, input().split())
    x.append(w)
    y.append(z)
print((max(x)-min(x))*(max(y)-min(y)))