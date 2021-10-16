import sys

res = []

def do(li):
    global res
    if li[0] == "push":
        res.append(li[1])
    elif li[0] == "pop":
        if res == []:
            print(-1)
        else:
            print(res.pop())
    elif li[0] == "size":
        print(len(res))
    elif li[0] == "empty":
        if res == []:
            print(1)
        else:
            print(0)
    elif li[0] == "top":
        if res == []:
            print(-1)
        else:
            print(res[-1])


for i in range(int(input())):
    do(list(sys.stdin.readline().split()))
