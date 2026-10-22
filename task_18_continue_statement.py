# Task 18 - continue (skip this round and go to the next)

# print only odd numbers
for n in range(1, 11):
    if n % 2 == 0:
        continue
    print(n, end=" ")
print()

# skip a letter
for ch in "programming":
    if ch == "m":
        continue
    print(ch, end="")
print()

# skip negative numbers while adding
nums = [4, -2, 7, -9, 10]
total = 0
for n in nums:
    if n < 0:
        continue
    total += n
print("sum of positives:", total)

# continue in while (careful to update the counter first or it loops forever)
i = 0
while i < 8:
    i += 1
    if i == 3 or i == 6:
        continue
    print("i is", i)

# skip blank lines
lines = ["hello", "", "world", "", "python"]
for line in lines:
    if line == "":
        continue
    print(line)
