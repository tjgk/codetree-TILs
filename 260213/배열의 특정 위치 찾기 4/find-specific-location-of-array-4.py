a=list(map(int,input().split()))
tf=0
t,s=0,0
for i in a:
    if i==0:
        print(t,s)
        tf=1
        break
    else:
        if i%2==0:
            t+=1
            s+=i
if tf==0: print(t,s)