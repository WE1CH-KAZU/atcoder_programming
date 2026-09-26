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

N = int(input())

S_list = input().strip().split(" ")

data_tuple = [
    (2, ["a", "b", "c"]),
    (3, ["d", "e", "f"]),
    (4, ["g", "h", "i"]),
    (5, ["j", "k","l"]),
    (6, ["m","n","o"]),
    (7, ["p","q","r","s"]),
    (8, ["t","u","v"]),
    (9, ["w","x","y","z"])
]

ans =[]
for i in range(N):
    moji = S_list[i][0]
    for value, li in data_tuple:
        if moji in li:
            ans.append(value)

print("".join(map(str, ans)))
