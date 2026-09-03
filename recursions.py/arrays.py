"largest element in array"
nums = [55, 32, -97, 3, 99, 67,100, 145]
largest = nums[0]
n = len(nums)
for i in range(0, n):
    largest = max(largest, nums[i])
print(largest)
