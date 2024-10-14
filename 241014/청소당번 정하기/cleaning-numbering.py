a,b,c=0,0,0
n=int(input())
for i in range(1,n+1):
    if i%12==0:
        c+=1
    elif i%3==0:
        b+=1
    elif i%2==0:
        a+=1
print(a,b,c)