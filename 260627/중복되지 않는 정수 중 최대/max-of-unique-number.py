n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
p=0

nums=nums[::-1]
for i in range(len(nums)):
    if nums.count(nums[i])==1:
        print(nums[i])
        p=-1
        break
if p==0:
    print(-1)