def unionArray(a, b):
        left = 0
        right = 0 
        result = []
        while left < len(a) and right < len(b):
            if a[left] < b[right]:
                if not result or result[-1] != a[left]:
                        result.append(a[left])
                left += 1
            elif b[right] < a[left]:
                if not result or result[-1] != b[right]:
                        result.append(b[right])
                right += 1
            else:
                if not result or result[-1] != a[left]:
                      result.append(a[left])
                left += 1
                right += 1
        
        while left < len(a):
            if result[-1] != a[left]:
                result.append(a[left])
            left += 1
        while right < len(b):
            if result[-1] != b[right]:
                result.append(b[right])
            right +=1

        return result

            
                          
                        
# print(unionArray([1, 2, 3, 4, 5], [1, 2, 7]))
# print(unionArray([10,100,101], [4]))
print(unionArray([3, 4, 6, 7, 9, 9], [1, 5, 7, 8, 8]))
