a=[int(i) for i in input().split()]
for i in range (len(a)):
    if a[i]>0 and a[i+1]>0 or a[i]<0 and a[i+1]<0:
        print(a[i], end=" ")
        print(a[i+1])
        break