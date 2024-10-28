a=int(input())
for i in range(1,a+1):
    if i%4==2:
        continue
    else:
        if (i//8)%2==0:
            continue
        else:
            if i%7<4:
                continue
            else:
                print(i,end=" ")