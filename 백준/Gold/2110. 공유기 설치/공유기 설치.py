import sys
def binary_search(ll,start,end):
    while start <= end:
        mid = (start + end) // 2
        prev = ll[0]
        count = 1

        for i in range(1, len(ll)):
            if ll[i] >= mid + prev:
                prev = ll[i]
                count += 1

        if count >= c: #작으면 늘려야 / 계속 저장
            global res
            start = mid + 1
            res = mid
        else:
            end = mid - 1

n,c = map(int,sys.stdin.readline().split())
ll = []
for i in range(n):
    x = int(sys.stdin.readline())
    ll.append(x)

ll.sort()
start = 0
end = ll[-1] - ll[0]
count = 0
binary_search(ll, start, end)
print(res)