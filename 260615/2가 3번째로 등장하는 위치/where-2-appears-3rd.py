n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(n):
    if a[i]==2:
        c+=1
        if c==3:
            print(i+1)
            break