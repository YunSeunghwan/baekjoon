resli = []
for i in range(int(input())):
    A, B = map(int, input().split())
    a, b = int(A), int(B)

    while a != b:  # 유클리드 호제법
        if a > b:
            a -= b
        else:
            b -= a

    resli.append(int(A * B / a))

for res in resli:
    print(res)
