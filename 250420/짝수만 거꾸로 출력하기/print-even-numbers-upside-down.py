n=int(input())
a=list(map(int,input().split()))
for i in list(reversed(list(filter(lambda x:x%2==0,a)))):
    print(i,end=" ")