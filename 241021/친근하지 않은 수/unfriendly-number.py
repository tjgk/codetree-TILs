s=0
for i in range(1,int(input())+1):
    if i%2==0 or i%3==0 or i%5==0:
        pass
    else:
        s+=1
print(s)