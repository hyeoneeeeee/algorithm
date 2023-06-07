import sys
n = int(sys.stdin.readline().strip())
card_dic = {}
for a in list(map(int, sys.stdin.readline().strip().split())):
    if a in card_dic:
        card_dic[a] += 1
    else:
        card_dic[a] = 1
m = int(sys.stdin.readline().strip())
for x in list(map(int, sys.stdin.readline().strip().split())):
    if x in card_dic:
        print(card_dic[x], end=" ")
    else:
        print(0, end=" ")
