n=int(input())
c=[0 for _ in range(10)]
a=list(map(int,input().split()))
for i in a:
    c[i]+=1
for i in range(9):
    print(c[i+1])