n=int(input())
i=0

while 2**i<n:
    i=i+1
if(2**i==n):
    print("YES")
else:
    print("NO")