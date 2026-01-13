start, end = map(int, input().split())

# Please write your code here.
t=0
for i in range(start,end+1):
    d=set()
    for j in range(1,i+1):
        if i%j==0:
            d.add(j)
    if len(d)==3:
        t+=1
print(t)