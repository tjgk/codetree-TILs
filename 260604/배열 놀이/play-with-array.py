n,q=map(int,input().split())
a=list(map(int,input().split()))
for i in range(q):
    b=list(input().split())
    if b[0]=="1":
        print(a[int(b[1])-1])
    elif b[0]=="2":
        if a.count(int(b[1]))!=0:
            print(a.index(int(b[1]))+1)
        else:
            print(0)  
    else:
        for i in range(int(b[1]),int(b[2])+1):
            print(a[i-1],end=" ")
        print()