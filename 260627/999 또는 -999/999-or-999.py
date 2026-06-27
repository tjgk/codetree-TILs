a=list(map(int,input().split()))
if 999 in a:
    a=a[:a.index(999)]
else:
    a=a[:a.index(-999)]
print(max(a),min(a))