arr=[int(i) for i in input().split()]

def minn(i):
    arr.sort()
    return arr[0]


print(minn(arr))