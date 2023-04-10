while True:
    a=int(input())
    l=[x for x in range(1,a) if a%x ==0]
    if sum(l)==a:
        print(f"{str(a)} = {' + '.join(map(str,l))}")
    elif a==-1:
        break
    else:
        print(f"{a} is NOT perfect.")