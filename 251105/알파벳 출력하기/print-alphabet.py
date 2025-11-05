n=int(input())
t=0
for i in range(n):
    for j in range(i+1):
        print(chr(65+t),end="")
        t+=1
        if t==26:
            t-=26
    print()