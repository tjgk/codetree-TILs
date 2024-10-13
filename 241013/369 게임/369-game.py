n=int(input())
for i in range(1,n+1):
    print(0 if i%3==0 or "3" in str(i) else i,end=" ")