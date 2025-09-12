n=int(input())
t=1
for i in range(n):
    for j in range(n):
        if i%2==0:
            print(t,end=" ")
            t+=1
        else:
            print(n*(i+1)-j,end=" ")
            t+=1
    print()