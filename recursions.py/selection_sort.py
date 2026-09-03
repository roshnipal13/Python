def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i],nums[min_idx] = nums[min_idx],nums[i]
nums = [2, 0, 2, 1, 1, 0, 1, 0, 1, 0]
selection_sort(nums)
print(nums)