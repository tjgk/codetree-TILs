n=int(input())
for i in range(n,0,-1):
    print("  "*(n-i),end="")
    print("* "*(2*i-1))
for i in range(n-1):
    print("  "*(n-2-i),end="")
    print("* "*(2*(i+1)+1))