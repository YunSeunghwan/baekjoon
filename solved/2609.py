A, B = map(int, input().split())
a, b = int(A), int(B)

while a != b:  # 유클리드 호제법
    if a > b:
        a -= b
    else:
        b -= a

print(b)
print(int(A * B / a))
