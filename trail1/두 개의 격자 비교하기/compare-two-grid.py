(N, M) = tuple(map(int, input().split()))

arr1 = [
    list(map(int, input().split()))
    for _ in range(N)
]

arr2 = [
    list(map(int, input().split()))
    for _ in range(N)
]

for r1,r2 in zip(arr1, arr2):
    for e1, e2 in zip(r1, r2):
        if e1 == e2:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()

