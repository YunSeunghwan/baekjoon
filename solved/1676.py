res = 0

for i in range(1,int(input())+1):
    if i % 125 == 0:
        res += 3
    elif i % 25 == 0:
        res += 2
    elif i % 5 == 0:
        res += 1
print(res)
