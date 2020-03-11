# -*- coding: utf-8 -*-
# No.841 8/32
# https://yukicoder.me/problems/no/841

S1, S2 = input().split()
day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

if S1 in day[5:7] and S2 not in day[5:7]:
    print('8/32')
elif S1 in day[5:7] and S2 in day[5:7]:
    print('8/33')
else:
    print('8/31')

# 22:57 - 23:04（AC）
