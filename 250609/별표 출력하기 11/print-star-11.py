n=int(input())
for i in range(n*2+1):
    if i%2==0:
        print("* "*(n*2+1))
    else:
        print("*   "*(n+1))