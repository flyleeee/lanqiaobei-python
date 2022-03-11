# import os
# import sys

# # 请在此输入您的代码
# word = input()
# d = {}
# for i in word:
#     d[i] = d.get(i, 0) + 1
# l = sorted(d.items(), key = lambda x: x[1], reverse = True)
# al = [l[0][0]]
# for i in range(len(l)):
#     if l[i][1] == l[i+1][1]:
#         al.append(l[i+1][0])
#     else:
#         break
# al.sort()
# print(al[0])
# print(l[0][1])
# 不知道为什么上面的通不过 真nm离谱
import os
import sys

# 请在此输入您的代码
word = input()
d = {}
for ii in word:
    d[ii] = d.get(ii, 0) + 1
l = sorted(sorted(d.items()), key = lambda x: x[1], reverse = True)

print(l[0][0])
print(l[0][1])
