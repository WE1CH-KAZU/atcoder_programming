"""
新規解答用のテンプレート
"""

import sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from heapq import heappop, heappush

input = sys.stdin.readline

INF = 10**18
MOD = 998244353

input = sys.stdin.readline

# 長さN,Q個のクエリ
N, Q = map(int, input().split())

# 0 vector
vec = [0] * N


# TRY 1====================
# この方法だとO(NQ)になって計算時間が終わらない
# for i in range(Q):
#     # クエリを取る
#     query = input().split()

#     if len(query) == 2:
#         # 2要素のクエリ
#         x = int(query[1])
#         # index 調整
#         vec[x -1] += 1

#     elif len(query) == 1:
#         # 1要素のクエリ
#         for l in range(N):
#             if vec[l] >= 1:
#                 vec[l] -= 1

#     xor = 0

#     for v in vec:
#         xor ^= v

#     print(xor)


# TRY 2 =======================
# # 引き算した回数をカウントする準備
# dec = 0
# # xor 初期値
# xor = 0

# for _ in range(Q):
#     # クエリ取得
#     q = input().split()

#     # query is 2
#     if len(q) == 2:
#         x = int(q[1])
#         # index 調整
#         x -= 1

#         # 古い値を取得
#         old_val = vec[x] - dec

#         # クエリ処理
#         vec[x] += 1

#         # 新しい値
#         new_val = vec[x] - dec

#         # xorを更新
#         # A xor B xor B = A を使う
#         xor ^= old_val
#         xor ^= new_val
    
#     else:
#         # 引き算する値を加算
#         dec += 1

#         # 結局0以上の値の要素のみ関係する

#         xor = 0

#         for i in range(N):

#             # 計算前の値
#             val = vec[i] - dec

#             # 0以下は0補正
#             val = max(val,0)
                
#             vec[i] = val + dec

#             xor ^= val
#     print(xor)


# 正の値を持つ index のリスト（重複させない）
# 元のコードは毎回 N 個すべてを見ていた。もし N が 20 万で、中身が正なのが 3 個だけだったら、19万9997 回は完全な無駄
# だから整数の部分の身を追いかけるposを用意する
pos = []
# xor 初期値
xor = 0
# 出力を溜めるリスト
out = []

for _ in range(Q):
    # クエリ取得
    q = input().split()

    # query is 2
    if len(q) == 2:
        # index調整
        x = int(q[1]) - 1

        v = vec[x]
        # 旧値を打ち消して新値を入れる
        # A xor B xor B = A を使う
        xor ^= v ^ (v + 1)
        # oldの結果を渡す
        vec[x] = v + 1

        # 0 から正になった瞬間だけ登録すれば重複しないので
        if v == 0:
            pos.append(x)

    else:
        # 正の要素だけを走査する
        # for で回すと0(N)になるので計算する部分だけをnew_posで追跡しながら計算する
        # 0 の要素は 1 を引いても 0 のままですし、XOR に 0 を混ぜても結果は変わらない。つまり 0 の要素は見るだけ無駄。
        new_pos = []           # 空箱用意
        for i in pos:          # 正の数の箱だけチェック
            v = vec[i]         # i番目の箱
            nv = v - 1         # クエリの指示を実行
            xor ^= v ^ nv      # v ^ nv (今 ^ 新) でxor(古)とxorを実行 
            vec[i] = nv        # 実際に上書き
            # 0 になったら次回以降は対象外
            if nv:             # nv がある(TRUE)ならば
                new_pos.append(i) # i番目にメモを追加
        pos = new_pos          # for文が全部終わったらposを上書き

    # 毎回出力すると遅いので、出力は溜めておいてまとめて出す。
    out.append(xor)            # Q個分のクエリの結果をoutに保存

# まとめて出力
print(*out, sep="\n")
