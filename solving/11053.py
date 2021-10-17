_ = input()
li = list(map(int, input().split()))
res = []
res.append(li[0])
for n in li[1:]:
    if res[-1] < n:
        res.append(n)
print(len(res))

# 반례 : 1 4 2 3 