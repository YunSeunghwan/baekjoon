a, b = map(int, input().split())
resli = []
while not (a == 0 & b == 0):
    if a % b == 0:
        resli.append('multiple')
    elif b % a == 0:
        resli.append('factor')
    else:
        resli.append('neither')
    a, b = map(int, input().split())
for x in resli:
    print(x)
