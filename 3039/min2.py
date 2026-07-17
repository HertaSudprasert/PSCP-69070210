"""min2"""

looper = int(input())
nums = []

while looper > 0:
    num = int(input())
    nums.append(num)
    looper -= 1

nums.sort()

print(nums[0])
