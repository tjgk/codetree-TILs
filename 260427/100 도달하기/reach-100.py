n=int(input())
a=[1,n]
while a[-1]<101:
    a.append(a[-1]+a[-2])
for i in a:
    print(i,end=" ")