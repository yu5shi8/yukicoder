# -*- coding: utf-8 -*-
# No.289 数字を全て足そう
# https://yukicoder.me/problems/no/289

import re

s = re.findall(r'[0-9]', input())
ans = sum([int(i) for i in s])
print(ans)

# str.isdigit(): を使えば、よりスマートになりそう
# ※全ての文字が数字なら真、そうでなければ偽
