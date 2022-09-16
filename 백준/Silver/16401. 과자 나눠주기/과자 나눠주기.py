m,n = map(int,input().split())
cookie = list(map(int,input().split()))
cookie.sort()

count = 0
start = 0
end = max(cookie)

while (start <= end):
    total = 0
    mid = (start + end) // 2
    
    for x in cookie:
        if x >= mid and mid != 0:
            total += x // mid
    
    if total < m:
        end = mid - 1
    
    else: 
        count = mid
        start = mid + 1
       
            
print(count)