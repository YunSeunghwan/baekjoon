#  각 집을 칠하는 경우의 수는 총 6가지가 있고, 데이터는 한줄에 N개씩 들어온다.

R = 0  # R을 먼저 칠한 경우
G = 0  # G를 먼저 칠한 경우
B = 0  # B를 먼저 칠한 경우

for i in range(int(input())):
    r = list(map(int, input().split()))
    g = list(map(int, input().split()))
    b = list(map(int, input().split()))
    R += r[i % 3]
    G += r[(i+1) % 3]
    B += r[(i+2) % 3]

print(min(R, G, B))