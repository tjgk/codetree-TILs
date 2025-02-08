n=int(input())
for i in range(n-1,-1,-1):
    print("  "*i+"* "*(n*2-1-i*2))
