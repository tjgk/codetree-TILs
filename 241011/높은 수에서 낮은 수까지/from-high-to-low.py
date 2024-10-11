a,b=map(int,input().split())
if a>b:
    a,b=b,a
for i in range(b,a-1,-1):
    print(i,end=" ")