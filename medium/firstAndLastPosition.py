def searchRange(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            for j in range(len(nums) - 1, -1, -1):
                if nums[j] == target:
                    return [i, j]
    return [-1, -1]
# Test Case
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))