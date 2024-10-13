a,b=map(int,input().split())
t=a
while t<=b:
    print(t,end=" ")
    if t%2==1:
        t*=2
    else:
        t+=3