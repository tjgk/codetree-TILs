start, end = map(int, input().split())

# Please write your code here.
s=0
for i in range(start,end+1):
    t=0
    for j in range(i):
        if i%(j+1)==0:
            t+=1
    if t==3:
        s+=1
print(s)