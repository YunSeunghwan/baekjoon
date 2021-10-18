# sdk = []
# for i in range(9):
#     sdk.append(list(map(lambda x: int(x), input().split())))

sdk = [
    [5, 0, 0, 0, 4, 0, 0, 8, 1],
    [0, 0, 4, 0, 5, 0, 2, 0, 0],
    [7, 1, 0, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 6, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 7, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 8, 0, 3, 9],
    [0, 0, 3, 0, 2, 0, 1, 0, 0],
    [8, 7, 0, 0, 9, 0, 0, 0, 5]
]

def checkCol(x, y):  # 세로줄 확인
    global sdk
    nums = []
    for _y in range(9):
        if sdk[_y][x] == 0:
            continue
        else:
            nums.append(sdk[_y][x])
    return nums


def checkRow(x, y):  # 가로줄 확인
    global sdk
    nums = []
    for _x in range(9):
        if sdk[y][_x] == 0:
            continue
        else:
            nums.append(sdk[y][_x])
    return nums


def checkBlock(x, y):  # 블록 확인
    global sdk
    nums = []
    xBlock = x // 3
    yBlock = y // 3
    for __x in range(3):
        for __y in range(3):
            _x = xBlock * 3 + __x
            _y = yBlock * 3 + __y
            if sdk[_y][_x] == 0:
                continue
            else:
                nums.append(sdk[_y][_x])
    return nums


def checkFilledNumber(x, y):
    nCol = checkCol(x, y)
    nRow = checkRow(x, y)
    nBlock = checkBlock(x, y)
    return list(set(nCol + nRow + nBlock))


def getCandidates(nFilled):
    a = list(range(1, 10))
    for i in nFilled:
        a.remove(i)
    return a


def step():
    global sdk
    for y in range(9):  # 세로줄
        for x in range(9):  # 가로줄
            if sdk[y][x] == 0:
                nFilled = checkFilledNumber(x, y)
                #print(x, y, getCandidates(nFilled))
                if len(nFilled) == 8:
                    sdk[y][x] = getCandidates(nFilled)[0]
                elif len(nFilled) == 0:
                    return 0
                else:  # 백트래킹
                    sdk_backup = sdk
                    for cand in getCandidates(nFilled):
                        sdk[y][x] = cand
                        step()
                    sdk = sdk_backup
    if sudoku_complete:
        return 0
    else:
        step()


def sudoku_complete():
    for row in sdk:
        for x in row:
            if x == 0:
                return 0
    return 1


step()

ans = sdk[:]
print(len(ans))
for i in range(9):
    ans[i] = list(map(lambda x: str(x), ans[i]))
for linn in ans:
    print(" ".join(linn))

# 이 방법으로는 답이 두개이상인 문제를 풀 수 없다.
# 백트래킹이 잘 작동하지 않는다. 오답처리됨.
