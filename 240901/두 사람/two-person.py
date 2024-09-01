s=False
for i in range(2):
    a,b=input().split()
    if int(a)>=19 and b=="M":
        s=True
print(1 if s==True else 0)