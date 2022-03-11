import collections

n, m, k, t = list(map(int,input().split()))
cnt = list(map(int, input().split()))
cnt.insert(0, 0)
kind = list(map(int, input().split()))
rule = collections.defaultdict(list)
best_rule = collections.defaultdict(list)
for i in range(k):                          #将规则用字典的形式表示
    f,m,s = list(map(int,input().split()))
    rule[s].append([f,m])
    #注意一下，两个作物杂交成一个作物是选择最长时间的，但是结果是需要最小时间的
def dfs(x):
    if x in kind:
        return 0
    min_time = float('inf')
    if best_rule[x] != []:
        return best_rule[x][2]

    for a, b in rule[x]:
        nt = max(dfs(a), dfs(b)) + max(cnt[a], cnt[b])
        if min_time > nt:
            min_time = nt
            best_a = a
            best_b = b
    best_rule[x] = [best_a, best_b, min_time]
    return min_time
    
print(dfs(t))