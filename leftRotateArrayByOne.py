def leftRotateArrayByOne(nums):
    first_val = nums[0]
    n = len(nums)
    for i in range(n-1):
        nums[i] = nums[i+1]
    nums[n-1] = first_val
    return nums

print(leftRotateArrayByOne([1, 2, 3, 4, 5]))
# print(leftRotateArrayByOne([6,7,8,9,10]))
# print(leftRotateArrayByOne([1,0,1,0,1,0]))
