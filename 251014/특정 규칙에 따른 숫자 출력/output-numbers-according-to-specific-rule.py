n=int(input())
t=0
for i in range(n):
    for j in range(n):
        if j+1<=i:
            print(" ",end=" ")
        else:
            t+=1
            if t==10:
                t=1
            print(t,end=" ")  
    print()