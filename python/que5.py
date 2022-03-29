number = input("Enter the four digit number: ")

reverse = number[::-1]

number = int(number)
reverse = int(reverse)

first_digit = reverse % 10

last_digit = number % 10

total_sum = first_digit + last_digit

print("Sum of first & last digit of %d is %d" % (number, total_sum))
