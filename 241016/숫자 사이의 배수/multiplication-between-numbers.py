s,t=0,0
a,b=map(int,input().split())
for i in range(a,b+1):
    if i%5==0 or i%7==0:
        s+=i
        t+=1
print(s,round(s/t,1))