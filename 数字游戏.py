from itertools import *
n, sum = (int(i) for i in input().split(' ')[:2])
def add(list):
    l = len(list) - 1
    for j in range(len(list) - 1):
        for i in range(l):
            list[i] = list[i] + list[i+1]
        l-=1
    return list[i]

for l in permutations(list(range(1, n+1))):
    if sum == add(list(l)):
        for i in l:
            print(i, end=' ')
        break

'''
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long LL;

const int N = 15;

int n, sum;
int y[N][N], a[N]; // y数组杨辉三角打表 a数组记录路径
bool vis[N];

void dfs(int cur, int s) // cur当前第几个数 s表示总数
{
    if (cur > n)
    {
        if (s == sum)
        {
            for (int i = 1; i <= n; i ++ ) cout << a[i] << ' ';
            exit(0);
        }
    }
    for (int i = 1; i <= n; i ++ )
    {
        if (!vis[i])
        {
            a[cur] = i;
            vis[i] = true;
            dfs(cur + 1, s + i * y[n][cur]); // s + 当前数 * 上图分析的杨辉三角系数
            vis[i] = false;                  // 为什么行是n 因为仔细推发现   
        }                                    // 图中的例题系数 1 3 3 1 正好对应杨辉三角第4行
    }                                        // 即第n行
}

int main()
{
    cin >> n >> sum;
    
    // 杨辉三角 打表
    y[1][1] = 1;
    for (int i = 1; i <= 13; i ++ )
        y[i][1] = 1, y[i][i] = 1;
    for (int i = 3; i <= 13; i ++ )
        for (int j = 1; j <= i; j ++ )
            y[i][j] = y[i - 1][j] + y[i - 1][j - 1];
    
    dfs(1, 0);
    return 0;
}

'''