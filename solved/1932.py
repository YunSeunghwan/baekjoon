N = int(input())
# s층 왼쪽에서 n번째 숫자 N_{s,n}까지의 합에 대해 최대값은
#   maxsum(N_{s,n})
# = max(
#     maxsum(N_{s-1,n-1}) + N_{s,n},
#     maxsum(N_{s-1,n}) + N_{s,n})
# maxsum은 이전단계만 저장하면 됨.
#   maxsum(N_{1,1})
# = max(
#     maxsum(N_{0,0}) + N_{1,1},
#     maxsum(N_{0,1}) + N_{1,1})
#   maxsum(N_{2,1})
# = max(
#     maxsum(N_{1,0}) + N_{2,1},
#     maxsum(N_{1,1}) + N_{2,1})
# n = 0 or n > s 인 경우 maxsum 은 0을 반환. -> 버려짐

SUM_LIST = []


def maxsum(s, n):
    if n <= 0 or n >= s:
        return 0
    else:
        return SUM_LIST[n-1]


for s in range(1, N+1):  # 1층에서 N층 까지
    nums = [0] + list(map(int, input().split()))  # len(nums) = s
    nSUM_LIST = []
    for n in range(1,s+1):
        nSUM_LIST.append(max(
            maxsum(s, n-1) + nums[n],
            maxsum(s, n) + nums[n]))
    # print("nSUM_LIST is : [", nSUM_LIST, "]")
    SUM_LIST = nSUM_LIST
print(max(SUM_LIST))
