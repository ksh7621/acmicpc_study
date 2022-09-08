import sys

n = sys.stdin.readline().rstrip()
ll = list(map(int,sys.stdin.readline().split()))

m = sys.stdin.readline().rstrip()
tt = list(map(int,sys.stdin.readline().split()))

dic = {}

for i in ll:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
        
for i in tt:
    if i in dic:
        print(dic[i], end = ' ')
    else:
        print(0, end = ' ')