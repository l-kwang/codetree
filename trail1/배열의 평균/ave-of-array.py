a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(sum(a)/len(a), sum(b)/len(b))
for i,j in zip(a,b):
    print((i+j)/2,end=' ')
print()
print((sum(a)+sum(b))/(len(a)+len(b)))