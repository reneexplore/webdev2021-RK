a=[int(i) for i in input().split()]
cnt=0
for i in range (1, len(a)-1):
    if a[i-1]<a[i] and a[i+1]<a[i]:
        cnt= cnt+1
print(cnt)