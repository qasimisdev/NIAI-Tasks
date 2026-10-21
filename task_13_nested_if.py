# Task 13 - nested if

i = 10
if i == 10:
    # first if inside
    if i < 15:
        print("i is smaller than 15")

    # nested if, only reached when the outer if is true
    if i < 12:
        print("i is smaller than 12 too")
    else:
        print("i is greater than or equal to 12")
