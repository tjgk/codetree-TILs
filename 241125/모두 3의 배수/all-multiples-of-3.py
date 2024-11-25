a=[]
for i in range(5):
    a.append(int(input()))
x=0
for i in a:
    if i%3!=0:
        print(0)
        x=1
        break
if x==0:
    print(1)