t=1
for i in range(int(input())):
    a,b=map(int,input().split())
    for j in range(a,b+1):
        t*=j
    print(t)
    t=1
