n=int(input())
t=0
for i in range(n):
    for j in range(n):
        t+=2
        print(t,end=" ")
        if t==8:
            t=0
    print()