N = int(input())

# sSUM[n] : n층에 한칸을 한번에 올라 온 경우의 최대점수합
# dSUM[n] : n층에 두칸을 한번에 올라 온 경우의 최대점수합
sSUM = [0]
dSUM = [0]

for n in range(1, N+1):
    s = int(input())
    if n == 1:
        sSUM.append(s)
        dSUM.append(s)
    else:
        sSUM.append(dSUM[n-1] + s)
        dSUM.append(max(
            sSUM[n-2] + s,
            dSUM[n-2] + s
        ))
print(max(sSUM[n], dSUM[n]))
