a=list(map(int,input().split()))
s,t=0,0
tf=0
for i in a:
    if i!=0:
        s+=i
        t+=1
    else:
        print(f"{s} {s/t:.1f}")
        tf=1
if tf==0: print(f"{s} {s/10:.1f}")