s=0
for i in range(4):
    a=list(map(int,input().split()))
    s+=sum(a[:i+1])
print(s)