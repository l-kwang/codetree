arr1 = [
    list(map(int, input().split()))
    for _ in range(3)
]

arr=list(map(int, input().split()))

arr2 = [
    list(map(int, input().split()))
    for _ in range(3)
]

for r1,r2 in zip(arr1, arr2):
    for e1, e2 in zip(r1, r2):
        result = e1 * e2
        print(result, end=' ')
    print()
