a=[]
for i in range(10):
    a.append(int(input()))
print(len(list(filter(lambda x:x%3==0,a))),len(list(filter(lambda x:x%5==0,a))))