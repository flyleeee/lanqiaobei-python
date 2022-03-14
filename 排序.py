def maopao(s):
    cnt = 0
    for i in range(1, len(s)):
        for j in range(len(s)-i):
            if s[j] > s[j+1]:
                temp = s[j]
                s[j] = s[j+1]
                s[j+1] = temp
                cnt += 1
    return cnt
from itertools import *
t = 'k'
l = list('abcdefghij')
l.append(t)
for i in range(26):
    for j in permutations(l):
        if maopao(list(j)) == 100:
            print(str(j))
        print(str(j))
    t = chr(ord(t) + 1)
    l.append(t)
# 这样遍历根本不行
import os
import sys

# 请在此输入您的代码
'''
全逆乱序的冒泡排序次数为N*(N-1)/2
15*14/2=105
14*13/2=91
100次交换至少需要15个字母
onmlkgihgfedcba
105-100=5,只需把第6个字母往后移到第1位即可
'''
print("jonmlkihgfedcba")