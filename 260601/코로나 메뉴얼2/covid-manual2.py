a,b,c,d=0,0,0,0
for i in range(3):
    x,y=input().split()
    y=int(y)
    if x=="Y":
        if y>=37:
            a+=1
        else:
            c+=1
    else:
        if y>=37:
            b+=1
        else:
            d+=1
print(a,b,c,d,end=" ")
if a>=2:
    print("E")