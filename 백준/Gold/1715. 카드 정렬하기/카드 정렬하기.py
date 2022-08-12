import heapq

n = int(input())

answer = 0
val = 0
heap = []

for i in range(n):
    data = int(input())
    heapq.heappush(heap,data)
    
while len(heap) != 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    
    val = first + second
    answer += val
    heapq.heappush(heap,val)
    
print(answer)