n = int(input())
x_list = list(map(int,input().split()))

ll = set(x_list)
ll = list(ll)
ll.sort()

dd = {}

for i in range(len(ll)):
    dd[ll[i]] = i
    
for i in x_list:
    print(dd[i], end = ' ')