def secondLargestElement(nums):
    nums.sort()
    n = len(nums)
    largest_number = nums[-1]
    second_largest = 0
    if n < 2:
        return -1
    for i in range(n-2, -1, -1):
        if nums[i] != largest_number:
            second_largest = nums[i]
            break
    return second_largest






print(secondLargestElement([8, 8, 8,8, 7, 6, 5]))