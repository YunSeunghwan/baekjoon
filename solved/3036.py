_ = input()

rings = list(map(int, input().split()))


def gcd(a, b):
    while a != b:  # 유클리드 호제법
        if a > b:
            a -= b
        else:
            b -= a
    return a


a = 1
b = 1

for i in range(len(rings)-1):
    a *= rings[i]
    b *= rings[i+1]
    while(gcd(a, b) != 1):
        g = gcd(a, b)
        a = int(a/g)
        b = int(b/g)
    print(str(a) + "/" + str(b))

