N = int(input())

DG = [1 for col in range(10)]
DG[0] = 0
# print(DG)

for order in range(1, N):
    _DG = [0 for col in range(10)]
    for _dg in range(10):
        if _dg == 0:
            _DG[_dg] = DG[1]
        elif _dg == 9:
            _DG[_dg] = DG[8]
        else:
            _DG[_dg] = DG[_dg - 1] + DG[_dg + 1]
    # print(DG, _DG)
    DG = _DG
# print(DG)
print(sum(DG) % (10 ** 9))
