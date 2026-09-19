n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

def function(list1, idx):
    if idx == 0:
        return
    else:
        max_val = max(list1)
        idx = list1.index(max_val)
        print(idx+1, end=' ')
        list1 = list1[0 : idx]
        return function(list1, idx)

function(a,len(a))