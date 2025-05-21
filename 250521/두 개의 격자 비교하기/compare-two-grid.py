n,m=map(int,input().split())
a,b=[],[]
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    b.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        print(0 if a[i][j]==b[i][j] else 1,end=" ")
    print()