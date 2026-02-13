t=0
for i in range(int(input())):
    a=list(map(int,input().split()))
    if sum(a)/4>=60:
        print("pass")
        t+=1
    else:
        print("fail")
print(t)