a=[]
while 1:
    a.append(int(input()))
    if a[-1]==0:
        break
for i in a[:-1]:
    print(i)