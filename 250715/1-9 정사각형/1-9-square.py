t=0
n=int(input())
for i in range(n):
    for j in range(n):
        t+=1
        print(t,end="")
        if t==9:
            t=0
    print()