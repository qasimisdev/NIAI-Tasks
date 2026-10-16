# Task 4 - add two numbers typed by the user

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# input gives text so convert to float first
total = float(num1) + float(num2)

print('The sum of {0} and {1} is {2}'.format(num1, num2, total))
