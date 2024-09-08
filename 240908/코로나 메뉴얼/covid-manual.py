a=0
for i in range(3):
    x,y=input().split()
    if x=="Y" and int(y)>=37:
        a+=1
print("E"if a>=2 else "N")