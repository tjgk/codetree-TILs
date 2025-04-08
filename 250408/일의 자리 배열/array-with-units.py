a,b=map(int,input().split())
t=[a,b]
for i in range(8):
    t.append((t[-1]+t[-2])%10)
print(" ".join(map(str,t)))
