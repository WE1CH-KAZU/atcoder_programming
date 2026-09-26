import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import (
    combinations,
    permutations,  # 順列組み合わせ
)

input = sys.stdin.readline
# 再起上限
sys.setrecursionlimit(10**6)

INF = 10**18
MOD = 998244353

def sosu_judge(n):
    # 素数かどうかを判定する
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5)+ 1):
        if n % d ==0:
            return False
    return True

N, D = map(int, input().split())

X_list = list(map(int, input().split()))

ans=[]
for i in range(N):
    ok = True
    for j in range(N):
        if i !=j and abs(X_list[i] - X_list[j]) < D:
            ok = False
            break
    if ok:
        ans.append(i+1)


print(len(ans))
print(" ".join(map(str, ans)))
