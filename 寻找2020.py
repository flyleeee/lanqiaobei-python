m = []
s = input()
while s != '':
    l = []
    for num in s:
        l.append(num)
    m.append(l)
    s = input()
l_i = len(m)
l_j = len(l)
cnt = 0

for i in range(l_i):
    for j in range(l_j):
        if j < l_j - 3:
            if m[i][j] == '2' and m[i][j+1] == '0' and m[i][j+2] == '2' and m[i][j+3] == '0' :
                cnt+=1
        if i < l_i - 3:
            if m[i][j] == '2' and m[i+1][j] == '0' and m[i+2][j] == '2' and m[i+3][j] == '0' :
                cnt+=1
        if j < l_j - 3 and i < l_i - 3:
            if m[i][j] == '2' and m[i+1][j+1] == '0' and m[i+2][j+2] == '2' and m[i+3][j+3] == '0' :
                cnt+=1
print(cnt)