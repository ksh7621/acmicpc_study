import sys
m,n = map(int, sys.stdin.readline().split())
#일단 정렬 안된거,,,
unord_planet = [list(map(int, sys.stdin.readline().split())) for i in range(m)]


iidx = []
ord_planet = []
count = 0

#정렬하고.......인덱스 리스트에 넣어서 비교
for i in range(m):
    ord_planet.append(sorted(unord_planet[i]))
    idx = []
    for j in unord_planet[i]:
        idx.append(ord_planet[i].index(j))
    iidx.append(idx)


for i in range(m-1):
    for j in range(i+1, m):
        if iidx[i] == iidx[j]:
            count += 1
print(count)