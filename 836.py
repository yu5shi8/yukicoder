# -*- coding: utf-8 -*-
# No.836 じょうよ
# https://yukicoder.me/problems/no/836

l, r, n = map(int, input().split())

mod = (r - l + 1) // n
num = (r - l + 1) % n

ans = [mod] * n
check = l % n

for i in range(num):
    if i + check > n - 1:
        ans[i + check - n] += 1
    else:
        ans[i + check] += 1

print(*ans, sep='\n')

# [1] 21:28 - 22:44（わかりませんでした）
# [2] 18:56 - 19:21 / 22:12 - 22:25（WA）- 22:35（WA）-（解答を閲覧）23:01
# [3] 14:18 - 
