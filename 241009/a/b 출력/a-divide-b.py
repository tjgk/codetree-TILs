import decimal
a,b=map(int,input().split())
decimal.getcontext().prec = 22
r=decimal.Decimal(a) / decimal.Decimal(b)
r=format(r, ".21f")
print(str(r)[:-1])