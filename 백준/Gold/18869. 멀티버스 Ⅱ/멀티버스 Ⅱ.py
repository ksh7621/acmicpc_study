import sys
m,n = map(int,sys.stdin.readline().split())
planets = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]
new_planets = [[] for _ in range(m)]
dic = {}

for i in range(m):
    sort_planets = sorted(list(set(planets[i])))

    for j in range(len(sort_planets)):
        dic[sort_planets[j]] = j

    for x in planets[i]:
        new_planets[i].append(dic[x])



new_planets.sort()


cnt, ans = 1, 0

for i in range(1,m):
    if new_planets[i] == new_planets[i-1]:
        cnt += 1
    else:
        ans += cnt * (cnt-1) // 2
        cnt = 1

ans += cnt * (cnt-1) // 2
print(ans)