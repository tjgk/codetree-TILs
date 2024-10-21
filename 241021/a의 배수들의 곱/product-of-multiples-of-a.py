a,b=map(int,input().split())
s=1
for i in range(a,b+1):
    if i%4==0:
        s*=i
print(s)