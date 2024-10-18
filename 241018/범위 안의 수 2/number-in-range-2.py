p,q=0,0
for i in range(10):
    t=int(input())
    if 0<=t<=200:
        p+=1
        q+=t
print(q,round(q/p,1))