def number_of_digits(num):
    no_of_digits = 0

    while num > 0:
        num = int(num/10)
        print(num)
        no_of_digits += 1
    print(no_of_digits)

number_of_digits(26)
number_of_digits(2634)