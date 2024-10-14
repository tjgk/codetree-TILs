a,b=0,0
for i in range(10):
    t=int(input())
    if t%3==0:
        a+=1
    if t%5==0:
        b+=1
print(a,b)