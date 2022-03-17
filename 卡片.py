from collections import *
d = defaultdict(int)
for i in range(10):
    d[str(i)] = 2021
def main():
    for i in range(1, 10000):
        for x in str(i):
            d[x] -= 1
            if d[x] == -1:
                print(i-1)
                return
                
main()