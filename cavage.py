import sys
sys.setrecursionlimit(10000)

testcase = int(input())
for _ in range(testcase):
    m,n,k = map(int,input().split())
    graph = [[0]*n for _ in range(m)]
    count=0

    for _ in range(k):
        a, b = map(int,input().split())
        graph[a][b]=1

    def dfs(x,y):
        if x<0 or y<0 or x>m-1 or y>n-1:
            return False

        if (graph[x][y] == 1):
            graph[x][y]=0
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return True
        else:
            return False
        return False

    for i in range(m):
        for j in range(n):
            if(dfs(i,j)==True):
                count=count+1
    print(count)
