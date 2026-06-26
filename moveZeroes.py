def move_zeroes(nums):
    list_zeroes = []
    n = len(nums)
    for i in range(n-1, -1, -1):
        if nums[i] == 0:
            list_zeroes.append(nums[i])
            nums.pop(i)
    print(nums)
    print(list_zeroes)
    return nums + list_zeroes

print(move_zeroes([0, 1, 4, 0, 5, 2]))