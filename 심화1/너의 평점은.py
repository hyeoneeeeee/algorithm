dic={"A+":4.5,"A0":4.0,"B+":3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0}
n=0
m=0
for _ in range(20):
    a=list(map(str, input().split()))
    if a[-1] == "P": pass
    else:
        m= m + float(a[-2])*dic[a[-1]]
        n= n + float(a[-2])
print(f"{m/n:.6f}")
