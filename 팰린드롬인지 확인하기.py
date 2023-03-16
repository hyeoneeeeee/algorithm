# a=input()
# for i in range(len(a)//2):
#     if a[i] == a[-i-1]:
#         pass
#     else:
#         print(0)
#         break
# else:
#     print(1)
    
# ...?
A=input()
print(+(A==A[::-1]))