# Task 23 - strings

s = "Machine Learning"
print(s)
print(len(s))
print(s[0], s[-1], s[0:7], s[::-1])

# case
print(s.upper(), s.lower(), s.title(), s.swapcase())

# find and replace
print(s.find("Learn"))
print(s.replace("Machine", "Deep"))
print(s.count("n"))
print(s.startswith("Mac"), s.endswith("ing"))

# split and join
words = s.split()
print(words)
print("-".join(words))

# strip
messy = "   hello   "
print("[" + messy.strip() + "]")

# formatting three ways
name, score = "ali", 91.456
print("name: %s, score: %.1f" % (name, score))
print("name: {}, score: {:.2f}".format(name, score))
print(f"name: {name}, score: {score:.0f}")

# checks
print("abc".isalpha(), "123".isdigit(), "abc123".isalnum())

# palindrome check
word = "madam"
print(word, "is palindrome:", word == word[::-1])

# count vowels
text = "artificial intelligence"
vowels = 0
for ch in text:
    if ch in "aeiou":
        vowels += 1
print("vowels:", vowels)

# strings can't be changed, a new one is made
t = "hello"
t = "J" + t[1:]
print(t)

# multi line
para = """first line
second line"""
print(para)
