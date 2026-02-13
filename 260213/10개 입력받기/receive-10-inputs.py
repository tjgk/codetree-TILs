a=list(map(int,input().split()))
s,t=0,0
for i in a:
    if i!=0:
        s+=i
        t+=1
    else:
        print(f"{s} {s/t:.1f}")