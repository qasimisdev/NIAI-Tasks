# Task 8 - area of a triangle from its three sides (heron's formula)

a = 5
b = 6
c = 7

# uncomment these to take input from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# semi-perimeter
s = (a + b + c) / 2

# area
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('The area of the triangle is %0.2f' % area)
