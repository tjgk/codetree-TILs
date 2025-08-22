n=int(input())
t=9
for i in range(n):
    for j in range(n):
        print(t,end="")
        t-=1
        if t==0:
            t=9
    print()