N, Q = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

for i in range(Q):
    a = list(map(int, input().split()))
    if a[0]==1:
        print(arr[a[1]-1])
    
    elif a[0]==2:
        if a[1] in arr:
            print(int(arr.index(a[1]))+1)
        else:
            print(0)

    elif a[0] == 3:
        # 방법 1: 리스트 슬라이싱과 print(*...) 활용 (추천)
        print(*arr[a[1]-1 : a[2]])
