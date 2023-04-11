t =[]
for _ in range(3):
    t.append(int(input()))
    set(t)
if sum(t) == 180:
    t = set(t)
    if len(t) ==1:
        print("Equilateral")
    elif len(t) ==2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print('Error')