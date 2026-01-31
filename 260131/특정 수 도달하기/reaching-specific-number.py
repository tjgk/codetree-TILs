a=list(map(int,input().split()))
s=0
t=0
for i in a:
    if i<250:
        s+=i
    else:
        print(f'{s} {s/a.index(i):.1f}')
        t=1
        break
if t==0:
    print(f'{s} {s/10:.1f}')