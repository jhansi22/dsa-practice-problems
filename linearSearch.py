def linear_search(nums,target):
    for index in range(len(nums)):
        if nums[index] == target:
            return index
    return -1

print(linear_search([2,2,3,4,3,5,6], 6))