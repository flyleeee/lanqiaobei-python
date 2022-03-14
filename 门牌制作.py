def gcd(a, b):
    if a < b:
        a, b = b, a
    while a % b != 0:
        a, b = b, a%b
    return b
cnt = 0
for i in range(1, 2021):
    for j in range(i, 2021):
        if gcd(i, j) == 1:
            cnt+=1 
print(cnt*2-1)