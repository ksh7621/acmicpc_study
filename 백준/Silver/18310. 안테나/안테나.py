n = int(input())

ll = list(map(int,input().split()))

ll= sorted(ll)

median = int((n-1)/2)
             
print(ll[median])