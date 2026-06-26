def missing_number(nums):
    n = len(nums)
    missing_number = 0
    for i in range(n+1):
        if i not in nums:
            missing_number = i
    return missing_number


print(missing_number([0, 2, 3, 1, 4]))
print(missing_number([0, 1, 2, 4, 5, 6]))
print(missing_number([1, 3, 6, 4, 2, 5]))
