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

S = input().strip()
s_shurui = sorted(set(S))

def sosu_judge(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5)+ 1):
        if n % d ==0:
            return False
    return True

# なかったら-1
ans = -1
# 10P種類で組み合わせ数
for i in permutations(range(10), len(s_shurui)):
    # (0,1)から昇順で組み合わせループ
    temp = dict(zip(s_shurui, i))
    # Sを左から順番に割り当てられている数字を取り出して合成
    T = "".join(str(temp[x]) for x in S)

    # 0除外
    if T[0] == "0":
        continue
    if sosu_judge(int(T)):
        ans = T
        break

print(ans)

