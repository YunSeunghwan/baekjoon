N = int(input())
nums = list(map(lambda x: int(x), input().split()))
op = list(map(lambda x: int(x), input().split()))

# 연산자 배치는 중복을 포함
# opt : 1,2,3,4 : +-*/
# N-1 자리 숫자를 자리수를 바꿔가면서 작은 수부터 나열, 모든 연산자 조합 획득


def solve():
    res_min = 1000000000
    res_max = -1000000000
    opt = get_first_opt()
    while opt != 'end':
        res = calculate_nums(opt)
        if res < res_min:
            res_min = res
        if res > res_max:
            res_max = res
        opt = get_next_opt(opt)
    print(res_max)
    print(res_min)
    return 0


def get_first_opt():
    res = '1' * op[0] + '2' * op[1] + '3' * op[2] + '4' * op[3]
    return res


def get_next_opt(opt):  # 1234 -> 1243
    for i in range(1, N-1):
        a = int(opt[-i])
        b = int(opt[-i-1])
        if a < b:
            opt[-i] = str(b)
            opt[-i-1] = str(a)
            return opt
    return 'end'


def divide(A, B):
    if A > 0:
        return A // B
    else:
        return -(-A // B)


def calculate(num1, num2, o):
    if o == '1':
        return num1 + num1
    elif o == '2':
        return num1 - num2
    elif o == '3':
        return num1 * num2
    elif o == '4':
        return divide(num1, num2)


def calculate_nums(opt):
    res = nums[0]
    for i in range(1, len(nums)):
        res = calculate(res, nums[i], opt[i-1])
    return res


solve()

