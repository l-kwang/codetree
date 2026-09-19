N1, N2 = tuple(map(int, input().split()))

A = list(map(int, input().split()))
B = list(map(int, input().split()))

if B[0] in A:
    A_startidx = A.index(B[0])
    A_endidx = A_startidx + len(B)
    
    is_match = True
    for i, j in zip(B, A[A_startidx:A_endidx]):
        if i != j:
            is_match = False
            break

    if is_match:
        print('Yes')
    else:
        print('No')
else:
    print('No')
