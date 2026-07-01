def reverse_number(num):
    rev_num = 0

    while num > 0:
        remainder = num % 10
        num = num // 10
        rev_num = rev_num * 10 + remainder
    return rev_num

print(reverse_number(25))
print(reverse_number(725))