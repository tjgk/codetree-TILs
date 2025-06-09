n=int(input())
print("* "*n)
for i in range(n-1):
    print("  "*(i+1),end="")
    if i%2==0:
        print("*   "*((n-i)//2))
    else:
        print("  * "*((n-i-1)//2))