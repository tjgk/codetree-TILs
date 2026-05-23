a=list(map(int,input().split()))
a=a[:a.index(0)]
c=[0 for i in range(11)]
for i in a:
    c[i//10]+=1
for i in range(10):
    print(f"{10*(10-i)} - {c[-1*(i+1)]}")