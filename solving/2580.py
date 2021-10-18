def solve_sdk():
    # ----------------------------
    # cell : 숫자 하나가 들어가는 셀
    # row : 가로줄
    # col :  세로줄
    # block 숫자 9개가 들어가는 3x3 칸
    # SDK : 스도쿠 판
    # Candidates : 후보를 적는 판
    # ----------------------------
    global SDK, Candidates, emptycells
    SDK = get_sudoku_problem()
    Candidates = SDK[:]
    emptycells = get_empty_cell_adresses()
    while emptycells != []:
        sdk_past = SDK[:]
        for cell in emptycells:
            get_candidates_oncell(cell)
        for cell in emptycells:
            if is_uniquecandidates(cell):
                fill_cell(cell, Candidates[cell[0]][cell[1]][0])
        if sdk_past == SDK:
            cell = emptycells[0]
            fill_cell(cell, Candidates[cell[0]][cell[1]][0])
    return SDK


def get_sudoku_problem():
    sdk = []
    for i in range(9):
        sdk.append(list(map(lambda x: int(x), input().split())))
    # sdk = [[0, 3, 5, 4, 6, 9, 2, 7, 8],
    #        [7, 8, 2, 1, 0, 5, 6, 0, 9],
    #        [0, 6, 0, 2, 7, 8, 1, 3, 5],
    #        [3, 2, 1, 0, 4, 6, 8, 9, 7],
    #        [8, 0, 4, 9, 1, 3, 5, 0, 6],
    #        [5, 9, 6, 8, 2, 0, 4, 1, 3],
    #        [9, 1, 7, 6, 5, 2, 0, 8, 0],
    #        [6, 0, 3, 7, 0, 1, 9, 5, 2],
    #        [2, 5, 8, 3, 9, 4, 7, 6, 0]]
    return sdk


def get_empty_cell_adresses():
    global SDK
    empty = []
    for i in range(9):
        for j in range(9):
            if SDK[i][j] == 0:
                empty.append([i, j])
    return empty


def get_candidates_oncell(cell):
    global Candidates
    cd = list(range(1, 10))
    cell_row = cell[0]
    cell_col = cell[1]
    bladr = get_adresses_onsameblock(cell)
    for i in range(9):  # 가로세로블록 중복확인해서 후보를 지우는 단계임!
        if i != cell_col:
            if SDK[cell_row][i] in cd:
                cd.remove(SDK[cell_row][i])  # 가로줄 후보 지우기
        if i != cell_row:
            if SDK[i][cell_col] in cd:
                cd.remove(SDK[i][cell_col])  # 세로줄 후보 지우기
        if bladr[i] != cell:             # 블록 후보 지우기
            if SDK[bladr[i][0]][bladr[i][1]] in cd:
                # print(i,cd)
                # print(SDK[bladr[i][0]][bladr[i][1]])
                cd.remove(SDK[bladr[i][0]][bladr[i][1]])
    Candidates[cell[0]][cell[1]] = cd
    return 0


def get_adresses_onsameblock(cell):
    cell_row = cell[0]
    cell_col = cell[1]
    bl_row = cell_row//3
    bl_col = cell_col//3
    bladr = []
    for i in range(9):
        adr_row = bl_row * 3 + i // 3
        adr_col = bl_col * 3 + i % 3
        bladr.append([adr_row, adr_col])
    return bladr


def is_uniquecandidates(cell):
    if len(Candidates[cell[0]][cell[1]]) == 1:
        return True
    else:
        return False


def fill_cell(cell, num):
    global SDK, Candidates, emptycells
    # 셀 채우기
    SDK[cell[0]][cell[1]] = num
    # 엠프티셀에서 지우기
    emptycells.remove(cell)
    # 같은 행열블록 후보지우기
    pass


ans = solve_sdk()

for i in range(9):
    ans[i] = list(map(lambda x: str(x), ans[i]))
for linn in ans:
    print(" ".join(linn))
