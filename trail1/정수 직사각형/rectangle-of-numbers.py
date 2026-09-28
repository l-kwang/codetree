(M,N) = tuple(map(int, input().split()))

arr = [
    [0 for _ in range(N)]
    for _ in range(M)
]

num = 1

for i in range(M):
    for j in range(N):
        arr[i][j] = num
        num+=1

for row in arr:
    for elem in row:
        print(elem, end=' ')    
    print()  

