from sys import stdin
input = stdin.readline

p, s, d = 0, 0, 0
for i in range(int(input())):
    w = int(input())
    p, s, d = max(s, d), p+w, s+w

print(max(p, s, d))

