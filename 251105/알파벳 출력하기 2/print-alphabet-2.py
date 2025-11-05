n=int(input())
t=0
for i in range(n):
    print("  "*i,end="")
    for j in range(n-i):
        print(chr(65+t),end=" ")
        t+=1
        if t==26:t-=26
    print()