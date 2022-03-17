n = int(input())
l = [tuple(map(int, input().split())) for i in range(n)]
l = list(set(l))
cnt = 2
for i in range(1, len(l)):
    a2 = l[i][0]
    b2 = l[i][1]
    s = set()
    for j in range(i):
        a1 = l[j][0]
        b1 = l[j][1]
        if a1 == a2:
            continue
        x = (b1-b2)/(a2-a1)
        y = a2*x+b2 # 这里用外面的a2和b2才行 不知道为什么
        s.add((x, y))
    cnt+=(len(s)+1)
print(cnt)