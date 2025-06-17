n=int(input())
if n>=1:
    print("* "*n)
for j in range(n-2):
    print("* "*(j+1)+"  "*(n-2-j),end="*\n")
if n>=2:
    print("* "*n)