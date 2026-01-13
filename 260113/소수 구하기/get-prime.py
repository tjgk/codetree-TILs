n=int(input())
t=[]
for i in range(1,n+1):
    a=[]
    for j in range(1,i+1):
        if i%j==0:
            a.append(j)
    if len(a)==2: t.append(i)
for i in t:
    print(i,end=" ")