a,b=map(int,input().split())
for i in range(4):
    for j in range(b,a-1,-1):
        print(f"{j} * {(i+1)*2} = {(i+1)*2*j}",end="")
        if j != a:
            print(" / ",end="")
    print()