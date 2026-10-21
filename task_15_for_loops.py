# Task 15 - for loops

# loop over a list
fruits = ["apple", "banana", "mango"]
for f in fruits:
    print(f)

# range
print("\ncounting 0 to 4")
for i in range(5):
    print(i)

# range with start, stop, step
print("\neven numbers from 2 to 10")
for i in range(2, 11, 2):
    print(i)

# loop over a string
print("\nletters in python")
for ch in "python":
    print(ch, end=" ")
print()

# loop over a dictionary
ages = {"ali": 20, "sara": 22, "bilal": 19}
print("\nages")
for name, age in ages.items():
    print(name, "is", age)

# sum of 1 to 100
total = 0
for n in range(1, 101):
    total += n
print("\nsum of 1 to 100 =", total)

# multiplication table of 7
print("\ntable of 7")
for n in range(1, 11):
    print("7 x", n, "=", 7 * n)

# for with else (else runs when loop was not broken)
for n in range(3):
    print(n)
else:
    print("loop finished normally")
