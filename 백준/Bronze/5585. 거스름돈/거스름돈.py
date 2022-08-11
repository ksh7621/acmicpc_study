coins = [500, 100,50, 10, 5, 1]

paper = 1000-int(input())

count = 0


for coin in coins:
    count += (paper // coin)
    paper %= coin
  
print(count)