start, end = map(int, input().split())

# Please write your code here.
t=0
for i in range(start,end+1):
    s=0
    for j in range(1,i):
        s+=j if i%j==0 else 0
    if s==i:
        t+=1
print(t)