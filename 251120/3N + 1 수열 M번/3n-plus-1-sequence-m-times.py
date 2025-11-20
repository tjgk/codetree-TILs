for i in range(int(input())):
    n=int(input())
    t=0
    while n!=1:
        if n%2==0:
            n//=2
        else:
            n=n*3+1
        t+=1
    print(t)