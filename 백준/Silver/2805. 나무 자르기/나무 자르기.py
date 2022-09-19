def binary_search(tree,start,end):
    res = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in tree:
            if i > mid:
                total += (i-mid)

        if total < m:
            end = mid - 1
        else:
            start = mid + 1
            res = mid
    return res

n,m = map(int,input().split())
tree = list(map(int,input().split()))

start = 0
end = max(tree)

print(binary_search(tree,start,end))