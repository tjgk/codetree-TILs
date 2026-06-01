a,b=map(int,input().split())
r=[0 for _ in range(b)]
while a>1:
    r[a%b]+=1
    a//=b
s=0
for i in r:
    s+=i*i
print(s)