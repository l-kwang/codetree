arr = list(map(int, input().split()))

sum_odd = 0

for i in range(0,len(arr),2):
    odd = arr[i]
    sum_odd+=odd

sum_even = 0

for i in range(1,len(arr),2):
    even = arr[i]
    sum_even+=even

print(abs(sum_odd-sum_even))