a,b,c,d=0,0,0,0
for i in list(map(int,input().split())):
    d+=1
    if d%2==0:
        a+=i
    if d%3==0:
        b+=i
        c+=1
print(f"{a} {b/c:.1f}")