a=list(map(int,input().split()))
if a.count(0)>0:
    a=a[:a.index(0)]
for i in reversed(a):
    print(i,end=" ")