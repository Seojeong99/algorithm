from collections import deque
n, m = map(int,input().split())
count=[0] * 100001

def bfs(start):
    que = deque([start])
    while(que):
     x = que.popleft()
     move = [x - 1, x + 1, x * 2]
     if(x==m):
        print(count[x])
        break;
     for i in range(len(move)):
        if 0<=move[i]<=100000 and count[move[i]]==0:
           count[move[i]]=count[x]+1
           que.append(move[i])


bfs(n)