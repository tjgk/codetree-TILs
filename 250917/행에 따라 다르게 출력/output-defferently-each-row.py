t=0
n=int(input())
for i in range(n):
    for j in range(n):
        if i%2==0:
            t+=1
            print(t,end=" ")
        else:
            t+=2
            print(t,end=" ")
    print()