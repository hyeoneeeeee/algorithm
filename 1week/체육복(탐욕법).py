def solution(n, lost, reserve):
    lost_list = lost[:]

    for num in lost:
        print(num)
        if num in reserve:
            reserve.remove(num)
            lost_list.remove(num)
        elif num == 1:
            reserve.remove(num+1)
            lost_list.remove(num)
        else:
            if num-1 in reserve:
                reserve.remove(num-1)
                lost_list.remove(num)
            elif num+1 in reserve:
                reserve.remove(num+1)
                lost_list.remove(num)
    print(n - len(lost_list))
    return n - len(lost_list)

solution(5, [2,4], [1, 2, 3, 5])