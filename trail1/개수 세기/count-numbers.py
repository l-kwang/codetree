arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

count = 0

for i in arr2:
    if arr1[1] == i:
        count+=1
print(count)