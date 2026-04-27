n=int(input())
i=0
c=0
while c!=2:
    i+=1
    print(n*i,end=" ")
    if n*i%5==0:
        c+=1