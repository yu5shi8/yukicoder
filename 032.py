# -*- coding: utf-8 -*-
# No.32 貯金箱の憂鬱
# https://yukicoder.me/problems/5

# 硬貨の枚数を入力
l = int(input())
m = int(input())
n = int(input())

# 後から見返してみると、if を毎度付けなくても良かった件
# 1円硬貨の場合
if n >= 25:
    m = m + (n // 25)
    n = n % 25

# 25円硬貨の場合
if m >= 4:
    l = l + (m // 4)
    m = m % 4

# 100円硬貨の場合
if l >= 10:
    l = l % 10

# 硬貨の合計数
coin_count = l + m + n
print(coin_count)

'''
【参考回答】
https://yukicoder.me/submissions/321110
l,m,n = [int(input()) for _ in '1'*3]
print(n%25 + (n//25+m)%4 + ((n//25+m)//4+l)%10)
'''