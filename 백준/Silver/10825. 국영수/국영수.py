n = int(input())
ll = []
for i in range(n):
    input_data = input().split()
    ll.append((input_data[0], int(input_data[1]), int(input_data[2]),int(input_data[3])))

ll = sorted(ll, key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in ll:
    print(i[0])