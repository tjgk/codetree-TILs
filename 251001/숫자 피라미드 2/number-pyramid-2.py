n=int(input())
s=0
for i in range(n):
    for j in range(i+1):
        s+=1
        print(s,end=" ")
    print()