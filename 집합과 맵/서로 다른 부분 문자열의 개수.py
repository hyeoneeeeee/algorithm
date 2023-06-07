s = input()
l = set()
for a in range(len(s)):
    for b in range(1,len(s)+1):
        l.add(s[a:b])
print(len(l)-1)