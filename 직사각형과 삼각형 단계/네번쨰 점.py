x = []
y = []
for _ in range(3):
    w,z = map(str, input().split())
    if w in x:
        x.remove(w)
    else:
        x.append(w)
    if z in y:
        y.remove(z)
    else:
        y.append(z)
print(*x,*y)