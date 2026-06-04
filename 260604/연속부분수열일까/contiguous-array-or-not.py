x,y=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
p=0
for i in range(x-y+1):
    if a[i:i+y]==b:
        p=1
        print("Yes")
if p==0:
    print("No")