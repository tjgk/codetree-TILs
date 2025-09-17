a,b=map(int,input().split())
for i in range(9):
    for j in range(b,a-1,-2):
        print(f"{j} * {i+1} = {j*(i+1)}",end="")
        if j!=a:
            print(" / ",end="")
    print()