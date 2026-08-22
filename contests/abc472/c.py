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

# N=日数
# M=直近の日数
# K=カロリーの合計
N, M, K = map(int, input().split())

A = list(map(int, input().split()))

# i日目のおやつAを食べたと仮定した時にmax(i-M+1, 1)日目からi日目までの
# 間に食べたおやつのカロリーの合計がK以下なら、i日目のおやつを実際に食べる
# そうではないならi日目のおやつを食べない
# つまりK以下になるんだったら、食べる時もある

# B[i] = 1日目からi日目までに実際に食べたカロリーの合計
tabeta = [0]*(N+1)
ans = []
for i in range(1,N+1):
    # 区間内に食べた分
    window = tabeta[i-1] - tabeta[max(i-M,0)]
    tabetai = A[i-1]
    estimate = window + tabetai
    if estimate <= K:
        tabeta[i] = tabeta[i-1] + A[i-1]
        ans.append('Yes')
    else:
        tabeta[i] = tabeta[i-1]
        ans.append('No')
    
print('\n'.join(ans))
