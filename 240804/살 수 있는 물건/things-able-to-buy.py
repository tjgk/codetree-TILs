n=int(input())
if n>=3000:
    print("book")
else:
    print("mask" if n>=1000 else "no")