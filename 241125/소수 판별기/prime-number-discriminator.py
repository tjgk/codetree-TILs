n=int(input())
x=0
for i in range(2,n+1):
    if n%i==0 and n!=i:
        x=1
        print("C")
        break
if x==0:
    print("P")