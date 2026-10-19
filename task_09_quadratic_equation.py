# Task 9 - solve ax^2 + bx + c = 0
# cmath so it still works when the answer is complex

import cmath

a = 1
b = 5
c = 6

# discriminant
d = (b ** 2) - (4 * a * c)

# two solutions
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print('The solution are {0} and {1}'.format(sol1, sol2))
