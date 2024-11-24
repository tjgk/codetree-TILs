a,b=map(int,input().split())
x=0
for i in range(a,b+1):
    if 1920%i==0 and 2880%i==0:
        print(1)
        x=1
        break
if x==0:
    print(0)