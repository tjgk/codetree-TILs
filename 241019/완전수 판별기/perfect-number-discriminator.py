s=0
n=int(input())
for i in range(1,n):
    if n%i==0:
        s+=i
print("P" if n==s else "N")