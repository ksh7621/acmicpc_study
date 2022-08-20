from collections import deque
def bfs(maps,x,y):
    answer = 1
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    queue = deque()
    queue.append((x,y))
    n,m = len(maps),len(maps[0])    
    nx = 0
    ny = 0
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y]+1
                queue.append((nx,ny))   
    
    return maps[n-1][m-1]            
        
    
def solution(maps):        
    answer = bfs(maps,0,0) 
    if answer == 1:
        return -1
    return answer