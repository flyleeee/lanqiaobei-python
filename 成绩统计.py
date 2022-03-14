n = int(input())
sl = []
j = 0
y = 0
for i in range(n):
    sl.append(int(input()))
    if sl[i] >= 60:
        j+=1
    if sl[i] >= 85:
        y+=1
print('{:}%'.format(round(j/n*100)))
print('{:}%'.format(round(y/n*100)))
