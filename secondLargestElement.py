def secondLargestElement(nums):
    n = len(nums)
    if n < 2:
        return -1
    nums.sort()
    largest = nums[-1]
    secondLargest = -1

    for i in range(n-2, -1, -1):
        if nums[i] != largest:
            secondLargest = nums[i]
            break
    return secondLargest



print(secondLargestElement([8, 8, 7, 6, 5]))