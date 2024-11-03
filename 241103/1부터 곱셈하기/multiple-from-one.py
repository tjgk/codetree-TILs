n=int(input())
s=1
for i in range(1,11):
    s*=i
    if s>=n:
        print(i)
        break