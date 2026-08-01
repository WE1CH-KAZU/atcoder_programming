# 任意の空白区切りの入力をlistに変換する

import sys

input = sys.stdin.readline

# 1個
N = int(input())

# 2個
A, B = map(int, input().split())

# 複数個（リスト）
A = list(map(int, input().split()))

# N行入力
A = [int(input()) for _ in range(N)]