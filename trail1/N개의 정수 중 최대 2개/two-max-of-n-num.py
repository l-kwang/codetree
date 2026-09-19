n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
max_val=max(a)
tmp=max_val
a.remove(max_val)
max_val=max(a)
print(f"{tmp} {max_val}")
