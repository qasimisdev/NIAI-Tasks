# Task 24 - sets (no duplicates, no order)

s = {1, 2, 3, 3, 2, 1}
print(s)

# remove duplicates from a list
dupes = [1, 5, 2, 5, 1, 9, 2]
print(list(set(dupes)))

# add / remove
s.add(10)
s.update([20, 30])
print(s)
s.remove(10)
s.discard(999)     # no error even if missing
print(s)

# membership is fast
print(2 in s)

# math with sets
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}
print("union:", a | b)
print("intersection:", a & b)
print("difference a-b:", a - b)
print("difference b-a:", b - a)
print("symmetric diff:", a ^ b)

# subset checks
print({1, 2}.issubset(a))
print(a.issuperset({1, 2}))
print({1, 2}.isdisjoint({8, 9}))

# empty set (not {} that makes a dict)
e = set()
print(type(e), type({}))

# unique letters in a word
print(sorted(set("mississippi")))

# common friends example
ali = {"sara", "bilal", "hina"}
sam = {"hina", "omar", "sara"}
print("common friends:", ali & sam)
