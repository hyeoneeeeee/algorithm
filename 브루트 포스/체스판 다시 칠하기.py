m,n=map(int, input().split())
c=[]
a=[]
for _ in range(m):
    c.append(input())
for i in range(m-7):
    for j in range(n-7):
        b_start=0
        w_start=0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l)%2 == 0:
                    if c[k][l] !='W':
                        w_start +=1
                    else:
                        b_start +=1
                else:
                    if c[k][l] != 'W':
                        b_start +=1
                    else:
                        w_start +=1
        a.append(b_start)
        a.append(w_start)
print(min(a))