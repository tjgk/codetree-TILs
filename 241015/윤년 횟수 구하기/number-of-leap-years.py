n=int((input()))
def year(x):
    if x%4==0:
        if x%100==0 and x%400!=0:
            return 0
        else:
            return 1
    else:
        return 0
t=0
for i in range(1,n+1):
    t+=year(i)
print(t)