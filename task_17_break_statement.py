# Task 17 - break

# stop at the first number divisible by 7
for n in range(1, 100):
    if n % 7 == 0:
        print("first multiple of 7 is", n)
        break

# stop when we find a letter
for ch in "machine learning":
    if ch == " ":
        print("found a space, stopping")
        break
    print(ch)

# search in a list
names = ["ali", "sara", "bilal", "hina"]
for name in names:
    if name == "bilal":
        print("found bilal")
        break
else:
    print("bilal not in list")

# break out of while True
n = 0
while True:
    n += 1
    if n * n > 200:
        break
print("first n with n squared over 200 is", n)

# break in nested loops only exits the inner loop
for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print("i =", i, "j =", j)
