a=int(input())
b=int(input())
for i in range(a, b+1):
    if pow(i, 0.5)==int(pow(i, 0.5)):
        print(i, end=" ")