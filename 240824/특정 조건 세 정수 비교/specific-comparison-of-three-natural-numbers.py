a,b,c=map(int,input().split())
if a==min([a,b,c]):
    print(1,end=" ")
else:
    print(0,end=" ")
print(1 if a==b==c else 0)