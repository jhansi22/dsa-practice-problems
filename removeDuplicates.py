def removeDuplicates(nums):
    n = len(nums)
    for i in range(n-1, -1, -1):
        if i > 0 and nums[i] == nums[i-1]:
            print(i, i-1)
            nums.pop(i)

    print(nums)

removeDuplicates([0,0,0,0,1,1,1,2,2,2,3,3])