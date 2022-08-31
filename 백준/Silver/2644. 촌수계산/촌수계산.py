n = int(input())
a,b = map(int,input().split())
m = int(input())
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)    

res = []
def dfs(graph,v,visited,cnt):
    visited[v] = True
    cnt += 1   
    
    if v == b:
        res.append(cnt)
    
    for i in graph[v]:        
        if not visited[i]:            
            dfs(graph,i,visited,cnt)
            
dfs(graph,a,visited,0)
            
if len(res) == 0:
    print(-1)
else:
    print(res[0]-1)