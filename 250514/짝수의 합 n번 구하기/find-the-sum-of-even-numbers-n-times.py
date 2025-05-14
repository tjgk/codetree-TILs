for i in range(int(input())):
    a,b=map(int,input().split())
    s=0
    for j in range(a,b+1):
        if j%2==0:
            s+=j
    print(s)