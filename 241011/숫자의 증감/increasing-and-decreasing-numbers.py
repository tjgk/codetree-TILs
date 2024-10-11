c,n=input().split()
if c=="A":
    for i in range(int(n)):
        print(i+1,end=" ")
else:
    for i in range(int(n),0,-1):
        print(i,end=" ")