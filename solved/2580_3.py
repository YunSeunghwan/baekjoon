import sys

Sdk = [list(map(int, input().split())) for _ in range(9)]
Zeros = [(i, j) for i in range(9) for j in range(9) if Sdk[i][j] == 0]


def get_possibles(x, y):
    possibles = set(range(1, 10))
    possibles -= set(Sdk[x])
    temp = set()
    for i in range(9):
        temp.add(Sdk[i][y])
    possibles -= temp
    temp = set()
    for _x in range(x//3*3, x//3*3+3):
        for _y in range(y//3*3, y//3*3+3):
            temp.add(Sdk[_x][_y])
    possibles -= temp
    return possibles
# print('zeros ; ', Zeros)
# print(get_possibles(6, 8))


def solve(n):
    if n == len(Zeros):
        [print(*row) for row in Sdk]
        sys.exit()
    x, y = Zeros[n]
    possibles = get_possibles(x, y)
    for num in possibles:
        Sdk[x][y] = num
        solve(n+1)
        Sdk[x][y] = 0


solve(0)