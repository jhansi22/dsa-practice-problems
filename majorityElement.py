def majority_element(nums):
    freq = {}
    for num in nums:
        if num not in freq:
            freq[num] = 0 
        freq[num] += 1
    max_value = 0
    print(freq)
    # for n, value in freq.items():
    #     if value > max_value:
    #         max_value = value
    #         majority_num = n
    # return majority_num
    return max(freq, key=freq.get)
        


print(majority_element([1, 1, 1, 2, 1, 2, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6]))