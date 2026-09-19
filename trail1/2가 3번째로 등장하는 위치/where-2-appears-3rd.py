N = int(input())
A = list(map(int, input().split()))

count=0
idx=0

for i in A:

    if i==2:
        count+=1

        if count == 3:
            print(idx+1)
    idx += 1

