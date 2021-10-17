M = {}


def next(n, i):
    global M
    # doit?
    if not (n in M):
        M[n] = 10**6
    if M[n] < i:
        return 0
    # print('next(', n, ",", i, ") called")
    # do
    M[n] = i
    if n == 1:
        return 1
    if n % 3 == 0:
        next(int(n/3), i+1)
    if n % 2 == 0:
        next(int(n/2), i+1)
    if (n % 3 != 0) or (n % 2 != 0):
        next(n-1, i+1)
    return 0


next(int(input()), 0)
print(M[1])
# 모든 경우의 수를 탐색하면서 메모.
