import sys
sys.setrecursionlimit(10000)

N, K = map(int, input().split())
MAT = [[0 for col in range(1001)] for row in range(1001)]


def C(n, k):
    if k == 0 or k == n:
        MAT[n][k] = 1
        return 1
    elif MAT[n][k] != 0:
        return MAT[n][k]
    else:
        MAT[n][k] = C(n-1, k) + C(n-1, k-1)
        return MAT[n][k]


print(C(N, K) % 10007)
