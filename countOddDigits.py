def count_odd_digits(num):
    count = 0
    remainder = 0
    quotient = 0
    while num > 0:
        remainder = num % 10
        num = num // 10
        if remainder % 2 != 0:
            count += 1
    return count







print(count_odd_digits(24))
print(count_odd_digits(25))
print(count_odd_digits(257))
print(count_odd_digits(257789))