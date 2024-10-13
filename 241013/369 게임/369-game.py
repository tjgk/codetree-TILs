n=int(input())
for i in range(1,n+1):
    print(0 if i%3==0 or str(i) in "3" else i,end=" ")