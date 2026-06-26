def largestElement(nums):
    max_number = nums[0]
    if len(nums) == 1:
        return nums[0]
    for i in nums:
        if i >= max_number:
            max_number = i
    return max_number
print(largestElement([3,3,6,4]))
print(largestElement([1,2,3,4]))
print(largestElement([-10]))
print(largestElement([-1,-2,-3,-4]))