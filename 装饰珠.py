from collections import *
zb = [list(map(int, input().split()))[1:] for i in range(6)]
m = int(input())
zhu = [list(map(int, input().split())) for i in range(m)]
kong = defaultdict(int)
cnt = 0
for i in zb:
    for j in i:
        kong[j]+=1
        cnt+=1

# https://blog.csdn.net/qq_51222650/article/details/115325860dfrrrrr