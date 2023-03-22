def searchInsert(nums, target):
    # using binary search
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right)
        guess = nums[mid]
        if guess == target:
            return mid
        if guess > target:
            right = mid - 1
        else:
            left = mid + 1
    return left
# Test Case
nums = [1, 3, 5, 6]
target = 7
print(searchInsert(nums, target))