a,b,c=map(int,input().split())
x=0
for i in range(a,b+1):
    if i%c==0:
        print("YES")
        x=1
        break
if x==0:
    print("NO")