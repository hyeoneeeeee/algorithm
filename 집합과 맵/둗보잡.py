import sys
n,m = map(int, sys.stdin.readline().strip().split())
people_set = set()
for _ in range(n):
    people_set.add(sys.stdin.readline().strip())
people_set2 = set()
for _ in range(m):
    people_set2.add(sys.stdin.readline().strip())
print(len(people_set & people_set2))
for x in sorted(list(people_set & people_set2)):
    print(x)
