N, price = map(int, input().split())
print(N, price)
coin = []

for i in range(N):
    coin.append(int(input()))

coin.reverse()
pp = int(price)
i = 0
n = 0
while pp != 0:
    if coin[i] <= pp:
        n += 1
        pp -= coin[i]
    else: 
        i += 1
print(n)