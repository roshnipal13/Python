nums = [55, 32, 97, -55, 45, 32, 88, 91]
n = len(nums)
largest = float("-inf")
s_largest = float("-inf")
for i in range(0, n):
    if nums[i] > largest:
        s_largest = largest
        largest = nums[i]

    elif nums[i] > s_largest and nums[i] != largest:
        s_largest = nums[i]
print(s_largest)
