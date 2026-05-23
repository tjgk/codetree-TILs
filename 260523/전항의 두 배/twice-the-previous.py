a=list(map(int,input().split()))
for i in range(8):
    a.append(a[-2]*2+a[-1])
for i in a:
    print(i,end=" ")