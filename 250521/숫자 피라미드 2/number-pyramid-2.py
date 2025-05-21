n=int(input())
t=0
for i in range(n):
    for j in range(i+1):
        t+=1
        print(t,end=" ")
    print()