# -*- coding: utf-8 -*-
# No.264 じゃんけん
# https://yukicoder.me/problems/699

n, k = map(int,input().split())

if n == k:
    print('Drew')
elif (n == 0 and k == 1) or (n == 1 and k == 2) or (n == 2 and k == 0):
    print('Won')
else:
    print('Lost')


'''
【参考回答】
https://yukicoder.me/submissions/328666

n, k = map(int,input().split())
if n == k:
    print("Drew")
else:
    if (n - k + 3) % 3 == 1:    # <= 負けの時は余りが必ず1…！！
        print("Lost")
    else:
        print("Won")
'''
