a,b=[],[]
for i in range(3):
    a.append(list(map(int,input().split())))

t=input()

for i in range(3):
    b.append(list(map(int,input().split())))

for i in range(3):
    for j in range(3):
        print(a[i][j]*b[i][j],end=" ")
    print()