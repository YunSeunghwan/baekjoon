 num_case = int(input())
counter = []
for case in range(num_case):
    pts = list(map(lambda x: int(x), input().split()))
    st = pts[:2]
    en = pts[2:]
    N = int(input())
    counter.append([0])

    for planet in range(N):
        pl = list(map(lambda x: int(x), input().split()))
        sip = ((pl[0]-st[0])**2 +(pl[1]-st[1])**2 < pl[2]**2)#st in planet
        eip = ((pl[0]-en[0])**2 +(pl[1]-en[1])**2 < pl[2]**2)
        counter[case] += abs(sip - eip)
    
for ct in counter:
    print(ct)