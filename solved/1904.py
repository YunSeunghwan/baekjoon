# a_n = a_{n-1} + a_{n-2]
# 근데 0으로 시작하는 숫자는 사실상 똑같음.
a, b = 0, 1
for i in range(int(input())):
    a, b = b, a+b
    if b > 15746:
        b -= 15746

print(b % 15746)
