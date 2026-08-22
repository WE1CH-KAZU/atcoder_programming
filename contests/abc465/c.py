import re
import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from itertools import (
    combinations,
    permutations,  # 順列組み合わせ
)

input = sys.stdin.readline

INF = 10**18
MOD = 998244353

N = int(input())
S = list(map(str, input().strip()))

A = deque()
reverse_judge = False # 反転していればTrue, そうでなければFalse

for i in range(1, N+1):
    # 最初に追加することはo, x 関係がないので追加する
    if reverse_judge == False:
        # 反転していない
        A.append(i)
    else:
        # 反転しているので、実質右側に追加するため
        A.appendleft(i)
    
    if S[i-1] == 'o':
        # 反転フラグがある場合
        if reverse_judge == False:
            reverse_judge = True
        else:
            reverse_judge = False

if reverse_judge == True:
    A.reverse()

print(*A)
