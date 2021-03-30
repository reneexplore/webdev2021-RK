v=int(input())
t=int(input())
s=v*t
if v>0:
    ost=int(s/109)
    print(s-(ost*109))
else:
    ost=int((-1*s)/109)
    print(109 + ost*109 + s)

