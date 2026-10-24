# Task 25 - dictionaries

student = {"name": "ali", "age": 21, "city": "lahore"}
print(student)
print(student["name"])
print(student.get("phone"))              # None, no crash
print(student.get("phone", "no phone"))  # custom default

# add / change
student["age"] = 22
student["course"] = "AI"
print(student)

# remove
student.pop("city")
del student["course"]
print(student)

# keys values items
print(list(student.keys()))
print(list(student.values()))
for k, v in student.items():
    print(k, ":", v)

# check key
print("name" in student)

# count words
text = "the cat and the dog and the bird"
counts = {}
for w in text.split():
    counts[w] = counts.get(w, 0) + 1
print(counts)

# dict comprehension
squares = {n: n * n for n in range(1, 6)}
print(squares)

# nested dictionary
school = {
    "ali": {"math": 80, "cs": 95},
    "sara": {"math": 90, "cs": 88},
}
print(school["sara"]["cs"])
for name, marks in school.items():
    print(name, "average:", sum(marks.values()) / len(marks))

# merge
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 30}
d1.update(d2)
print(d1)

# sort by value
scores = {"ali": 70, "sara": 95, "bilal": 82}
for name in sorted(scores, key=scores.get, reverse=True):
    print(name, scores[name])
