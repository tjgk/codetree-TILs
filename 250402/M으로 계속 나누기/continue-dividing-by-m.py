N, M = map(int, input().split())

# Please write your code here.
while N>=M:
    print(N)
    N//=M
print(N)