a=["apple","banana","grape","blueberry","orange"]
s=input()
c=0
for i in a:
    if i[3]==s or i[2]==s:
        print(i)
        c+=1
print(c)