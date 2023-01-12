def solution(n, lost, reserve):
    lost_list = [x for x in lost if x not in reserve]
    reserve_list = [y for y in reserve if y not in lost]
    for num in reserve_list:
        forward = num + 1
        back = num - 1
        if back in lost_list:
            lost_list.remove(back)
        elif forward in lost_list:
            lost_list.remove(forward)

    return n-len(lost_list)

solution(5, [2,4], [1, 2, 3, 5])