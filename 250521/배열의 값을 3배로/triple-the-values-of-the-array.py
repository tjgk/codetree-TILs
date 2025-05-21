a=[]
for i in range(3):
    a.append(list(map(int,input().split())))
for i in a:
    for j in i:
        print(j*3,end=" ")
    print()