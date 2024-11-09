a={1:"John",2:"Tom",3:"Paul",4:"Sam"}
while 1:
    t=int(input())
    if t in a:
        print(a[t])
    else:
        print("Vacancy")
        break