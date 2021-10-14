res = []
PD = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
# len(PD) = 11
# PD_6 = PD_1 + PD_5
# PD_{n-1} = PD_{n-6} + PD_{n-2}


def cal_PD():
    global PD
    PD.append(PD[-5] + PD[-1])


for i in range(int(input())):  # T
    N = int(input())
    while (len(PD) < N+1):
        cal_PD()
    res.append(PD[N])

for r in res:
    print(r)
