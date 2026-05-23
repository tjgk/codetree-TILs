a=list(map(int,input().split()))
a=a[:a.index(0)]
c=[0 for i in range(10)]
for i in a:
    c[i//10]+=1
for i in range(9):
    print(f"{i+1} - {c[i+1]}")
