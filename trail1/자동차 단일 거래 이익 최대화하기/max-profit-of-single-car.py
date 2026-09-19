n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
max_diff = 0

for i in range(0,len(price)+1):
    for j in price[i+1:]:
        result = j - price[i]
        if result > max_diff:
            max_diff = result
print(max_diff)
