from sys import stdin
from itertools import combinations as comb
input = stdin.readline



def main():  # N개의 숫자중K개를 선택, 서로소인지 확인 후 결과 print
    global N, K
    N, K = map(int, input().split())
    Num = list(map(int, input().split()))
    print('xptmxmdyd')
    res = 0
    for chosen_idx in comb(list(range(N)), K):
        numbers = list(map(lambda x: Num[x], chosen_idx))
        # print('idx : ', chosen_idx)
        # print('numbers : ', numbers)
        # print('   is Copirme : ', isCoprime(numbers))
        if isCoprime(numbers):        
            res += 1
    return res


def init_chosen_idx():
    return list(range(K))
# print(init_chosen_idx())


def isEndOfCombination(chosen_idx):
    return chosen_idx == list(range(N-K, N))
# print(isEndOfCombination(list(map(int, input().split()))))

def next_chosen_idx(chosen_idx):
    #K개의 수열을 받으면 아랫자리(o = k)부터 다음숫자로. 다음숫자가 없을경우(o = N - K - 1)인 경우 그 바로 윗자리를 다음숫자로 옮기고, 자신과 자신 아래의 숫자를 그 옆에 나란히 옮긴다.
    pass



def isCoprime(args):  # K-채완수열인가?
    def mcd(b, a):  # 최대공약수 구하기
        while a != b:  # 유클리드 호제법
            if a > b:
                a -= b
            else:
                b -= a
        return b

    if len(args) != K:
        raise Exception('변수의 개수(' + str(len(args)) + ') 가 K(' + str(K) + ')와 다릅니다')
        
    for i in range(K):
        if i == 0: mcd_now = args[0]
        else: mcd_now = mcd(mcd_now , args[i])
        # print(mcd_now)
        if mcd_now == 1:    
            return True
    return False
N, K = 1, 2
# print(isCoprime(list(map(int, input().split()))))

print(main())

# 이거하면 시간초과넹 ㅜ