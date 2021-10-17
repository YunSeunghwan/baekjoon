# 전 단계에서 r,g,b를 칠한 경우에 대해 가장 높은 점수만 남기기.

N = int(input())
_r, _b, _g = 0, 0, 0


def slt(*args): return min(*args)


for i in range(N):
    r, g, b = map(int, input().split())
    _r, _g, _b = slt(_g + r, _b + r), slt(_r + g, _b + g), slt(_r + b, _g + b)
print(slt(_r, _b, _g))
