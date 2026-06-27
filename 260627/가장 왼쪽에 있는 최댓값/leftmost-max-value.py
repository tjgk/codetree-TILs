n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
while 1:
    p=max(a)
    if a[0]==p:
        print(1)
        break
    print(a.index(p)+1,end=" ")
    a=a[:a.index(p)]