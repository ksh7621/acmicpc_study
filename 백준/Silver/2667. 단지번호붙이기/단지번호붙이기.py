n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))


total_cnt = []


def dfs(x,y):
    global part_cnt
    if x < 0 or y < 0 or x>=n or y>=n:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 2
        part_cnt += 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)        
        return True
    return False

res = 0
part_cnt = 0

for i in range(n):
    for j in range(n):       
        if dfs(i,j) == True:
            total_cnt.append(part_cnt)
            res += 1
            part_cnt = 0
            
print(res)
total_cnt.sort()
for i in range(len(total_cnt)):
    print(total_cnt[i])