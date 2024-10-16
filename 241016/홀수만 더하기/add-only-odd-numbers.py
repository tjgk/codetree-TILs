s=0
for i in range(int(input())):
    x=int(input())
    if x%2==1 and x%3==0:
        s+=x
print(s)