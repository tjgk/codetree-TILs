n=int(input())
for i in range(n):
    n//=(i+1)
    if n<=1:
        print(i+1)
        break