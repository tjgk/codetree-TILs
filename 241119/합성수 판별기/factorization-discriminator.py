tf=False
n=int(input())
for i in range(2,n):
    if (n//i)%2==0:
        tf=True
        break
print("C" if tf==1 else "N")