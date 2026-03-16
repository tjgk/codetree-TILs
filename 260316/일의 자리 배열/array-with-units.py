a=list(map(int,input().split()))
for i in range(8):
    a.append(a[-1]+a[-2])
for i in a:
    print(i%10,end=" ")