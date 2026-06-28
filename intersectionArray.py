def intersection_array(nums1, nums2):
    left = 0
    right = 0
    result = []
    while left < len(nums1) and right < len(nums2):
        if nums1[left] == nums2[right]:
            if not result or result[-1] != nums1[left]:
                result.append(nums1[left])
            left += 1
            right += 1
        elif nums1[left] < nums2[right]:
            left +=1
        elif nums2[right] < nums1[left]:
            right +=1
    return result

print(intersection_array([1, 2, 2, 3, 5], [1, 2, 7]))
print(intersection_array([10,100,101], [4]))
print(intersection_array([3, 4, 6, 7, 8, 8], [1, 7, 8, 8]))


