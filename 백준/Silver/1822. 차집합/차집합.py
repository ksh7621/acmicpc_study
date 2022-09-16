na,nb = map(int,input().split())

a = list(map(int,input().split()))
b = list(map(int,input().split())) 
        
seta = set(a)
setb = set(b)

setc = list(seta-setb)
setc.sort()

print(len(setc)) 

for i in setc:
    print(i, end = ' ')