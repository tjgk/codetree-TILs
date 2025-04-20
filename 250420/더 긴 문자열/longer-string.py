a,b=input().split()
if len(a)==len(b):
    print("same")
else:
    print(a if len(a)>len(b) else b, max(len(a),len(b)))