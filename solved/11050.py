n, k = map(int, input().split())
res = 1
for i in range(1, k+1):
    res *= n - i + 1
    res /= i
print(int(res))
