arr=input().split()
a=int(arr[0])
n=int(arr[1])

def power(a,n):
    if a==n:
        return 0
    else:
        return 1


print(power(a,n))