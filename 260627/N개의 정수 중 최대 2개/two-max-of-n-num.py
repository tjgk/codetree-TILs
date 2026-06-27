n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
a.sort()
print(a[-1],a[-2])