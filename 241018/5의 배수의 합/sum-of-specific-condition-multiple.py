s=0
a,b=map(int,input().split())
for i in range(min(a,b),max(a,b)+1):
    if i%5==0:
        s+=i
print(s)