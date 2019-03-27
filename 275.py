# -*- coding: utf-8 -*-
# No.275 中央値を求めよ
# https://yukicoder.me/problems/no/275

n = int(input())
a = list(map(int, input().split()))
a.sort()
median = 0

if n % 2 == 0:
    while len(a) > 2:
        del a[0]
        del a[-1]
    calc = (a[0] + a[1]) / 2
    median = round(calc, 1)
else:
    while len(a) > 1:
        del a[0]
        del a[-1]
    median = a[0]

print(median)
