c=0
for i in range(int(input())):
    if i%2!=0 and i%3!=0 and i%5!=0:
        c+=1
print(c)