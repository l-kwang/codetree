a = list(map(int, input().split()))
under_500=[]
over_500=[]
for i in a:
    if i<500:
        under_500.append(i)
    else:
        over_500.append(i)
print(f"{max(under_500)} {min(over_500)}")