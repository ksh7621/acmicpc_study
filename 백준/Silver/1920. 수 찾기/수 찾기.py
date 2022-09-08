def binary_search(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return 0

n = int(input())
ll = list(map(int,input().split()))
ll.sort()

m = int(input())
x = list(map(int,input().split()))

for i in x:
    result = binary_search(ll, i, 0, n-1)

    print(result)