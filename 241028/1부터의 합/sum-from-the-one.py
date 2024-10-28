n=int(input())
s=0
for i in range(1,101):
    if s+i>=n:
        print(s)
        break
    else:
        s+=i