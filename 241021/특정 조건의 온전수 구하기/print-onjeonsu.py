for i in range(1,int(input())+1):
    if i%2==1 and i%10!=5 and (i%3!=0 or i%9==0):
        print(i,end=" ")