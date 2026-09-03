"Check array is sorted or not if that is sorted print true other bise false"
nums = [ 3, 40, 6, 8, 9, 10, 20]
n= len(nums)
for i in range(0, n-1):
    if nums[i]>nums[i+1]:
        print (False)
print (True)