def findMaxConsecutiveOnes(nums):
    temp = 0
    max_value = 0
    for i in nums:
        if i == 1:
            temp += 1
        else:
            if temp > max_value:
                max_value = temp
                temp = 0
    if temp > max_value:
        max_value = temp
    return max_value

def findMax(nums):
    temp = 0
    max_value = 0
    for num in nums:
        if num == 1:
            temp += 1
            max_value = max(temp, max_value)
        else:
            temp = 0
    return max_value
        



print(findMaxConsecutiveOnes([1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1]))