N = int(input())
f = list(map(int, input().split()))  # factor

if len(f) == 1:
    N = f[0] ** 2
else:
    N = min(f) * max(f)
    
print(N)


