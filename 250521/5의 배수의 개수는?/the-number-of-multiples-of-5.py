cnt=0
for i in range(4):
    for j in list(map(int,input().split())):
        if j%5==0:
            cnt+=1
print(cnt)