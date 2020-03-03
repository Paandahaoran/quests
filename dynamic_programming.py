import numpy as np

'''
从递归讲起的动态规划问题
'''

'''1.递归举例，斐波那契数列，用递归树分析复杂度'''

def fib(N):
    if (N == 1 or N == 2):
        return 1
    else:
        return fib(N-2) + fib(N-1)
#print(fib(36))
'''2.备忘录递归剪纸降低复杂度'''
import numpy as np
def fib_memo(N):
    memo = np.zeros(10000)
    memo[1] = memo[2] = 1
    return memo_cal(memo,N)


def memo_cal(memo,N):
    if memo[N] == 0:
        memo[N] = memo_cal(memo,N-2)+memo_cal(memo,N-1)
    return memo[N]

print(fib_memo(1400))



'''空间优化'''

def fib_opt(N):
    if N < 2:
        return N
    prev = 0
    curr = 1
    for i in range(1,N):
        sum = prev + curr
        prev = curr
        curr = sum
    return sum



print (fib_opt(1000))




'''凑零钱'''
conintype = [1,2,5,10,20,50,100]
#k = coin type n = price
def coincharge(k,n):
    if k >7 and k<=0 :
        print("error")
        return -1
    kl = conintype[0:k]
    coin_number = 0
    rest = n
    while(rest != 0):
        if rest >= kl[-1]:
            rest -= kl[-1]
            coin_number += 1
        else:
            for i in range(-2,-len(kl),-1):
                if rest >= kl[i] and rest < kl[i+1]:
                    rest -= kl[i]
                    coin_number += 1
    return coin_number

print(coincharge(6,1922303910))
