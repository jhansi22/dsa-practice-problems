def largestElement(nums):
    largest_num = 0
    if len(nums) < 2:
        return nums[0]
    for num in nums:
        if num > largest_num:
            largest_num = num
    return largest_num
print(largestElement([3,3,6,4]))
print(largestElement([1,2,3,4]))
print(largestElement([-10]))
print(largestElement([-1,-2,-3,-4]))