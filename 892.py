# -*- coding: utf-8 -*-
# No.892 タピオカ
# https://yukicoder.me/problems/no/892

A1, B1, A2, B2, A3, B3 = map(int, input().split())

if (A1 + A2 + A3) % 2 == 0:
    print(':-)')
else:
    print(':-(')

# 17:31 - 17:34（TLE）- 17:37（AC）
