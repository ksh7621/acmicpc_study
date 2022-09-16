def binary_search(array, target, start, end):
    mid = (start+end)//2
    
    while start<=end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1    
    return 0



n = int(input())
ll1 = list(map(int,input().split()))
ll1.sort()

m = int(input())
ll2 = list(map(int, input().split()))

answer = []

for i in range(len(ll2)):
    res = binary_search(ll1, ll2[i], 0, len(ll1)-1)
    answer.append(res)
        
for i in answer:
    print(i, end = ' ')    