c=[0 for _ in range(7)]
a=list(map(int,input().split()))
for i in a:
    c[i]+=1
for i in range(6):
    print(f"{i+1} - {c[i+1]}")