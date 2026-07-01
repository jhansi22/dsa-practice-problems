def largestDigit(n):
    largest_num = 0
    while n > 0:
        remainder = n % 10
        n = n // 10
        if remainder > largest_num:
            largest_num = remainder
    return largest_num

print(largestDigit(4))
print(largestDigit(24))
print(largestDigit(297))
print(largestDigit(2789898888))