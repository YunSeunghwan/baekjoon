import itertools as it

N = int(input())
nums = list(map(lambda x: int(x), input().split()))
op = list(map(lambda x: int(x), input().split()))


def solve():
    res_min = 10**9
    res_max = -10**9
    firstopts = ['1']*op[0] + ['2']*op[1] + ['3']*op[2] + ['4']*op[3]
    for opt in it.permutations(firstopts, N-1):
        res = calculate_nums(opt)
        if res < res_min:
            res_min = res
        if res > res_max:
            res_max = res
    print(res_max)
    print(res_min)
    return 0


def calculate(num1, num2, o):
    if o == '1':
        return num1 + num2
    elif o == '2':
        return num1 - num2
    elif o == '3':
        return num1 * num2
    elif o == '4':
        if num1 > 0:
            return num1 // num2
        else:
            return -(-num1 // num2)


def calculate_nums(opt):
    res = nums[0]
    for i in range(1, len(nums)):
        res = calculate(res, nums[i], opt[i-1])
    return res


solve()

