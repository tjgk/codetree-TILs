a,b,c=0,0,0
for i in list(map(int,input().split())):
    if i%2==0:
        a+=i
    if i%3==0:
        b+=i
        c+=1
print(f"{a} {b/c:.1f}")