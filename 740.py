# -*- coding: utf-8 -*-
# No.740 幻の木
# https://yukicoder.me/problems/no/740

n, m, p, q = map(int, input().split())
leaf = 0
i = 0

while leaf < n:
    i += 1
    check = i % 12
    if p <= check <= p + q - 1:
        leaf += m * 2
    elif i % 12 == 0 and p + q - 1 == 12:
        leaf += m * 2
    else:
        leaf += m
    if leaf == n:
        break

print(i)

# 9:42 - 
