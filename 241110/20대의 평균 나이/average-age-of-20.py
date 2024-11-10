a=[]
while 1:
    n=int(input())
    if n>=30:
        print(f'{sum(a)/len(a):.2f}')
        break
    else:
        a.append(n)