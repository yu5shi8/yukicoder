# -*- coding: utf-8 -*-
# No.207 世界のなんとか
# https://yukicoder.me/problems/560

a, b = map(int, input().split())
b = b + 1
lst = [i for i in range(a, b)]

for i in lst:
    if i % 3 == 0:
        print(i)
    elif '3' in str(i):    # str(i).find('3')>=0 のようにカッコ良く書こう
        print(i)
    else:
        pass

'''
【参考回答】
https://yukicoder.me/submissions/325611
valueMin,valueMax = map(int, input().split()) 

for i in range(valueMin,valueMax+1):
    if ( (i%3)==0 or str(i).find('3')>=0):
        print(i)
'''