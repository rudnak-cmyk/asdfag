import math
a = 88
b = '14'
print(a+int(b))
print(a-int(b))
print(a*int(b))
print(a/int(b))
print(math.pi * 5)

text = ' Hello, Python! '
text = text.strip()
text = text.replace('!', '?')
text = text.upper()
print(text)

text = text.lower().replace('?', '!')
print(text)
assert text == 'hello, python!'

numbers = [7,2,5]
numbers.append(4)
numbers.insert(1,10)
numbers.extend([1,1,1])
numbers.remove(7)
pop = numbers.pop()
numbers.sort()
numbers.reverse()
print(numbers.count(2))
print(numbers.index(1))
copy = numbers.copy()
numbers.clear()
print(copy)
print(numbers)

t = (1,2,3)
z = (4,5)
t2 = t + z
print(t2)
print(t2.count(3))
print(t2.index(4))
print(t)

values = [3,1,3,2,1,5,2]
unique_values = set(values)
print(unique_values, len(unique_values))
other = {2,4,5}
print(unique_values & other)
print(unique_values | other)
print(unique_values - other, other - unique_values)

scores = {"Alice":85, "Bob":90}
scores['Charlie'] = 78
print(scores)
scores['Bob'] = 95
print(scores.get('Dave'))
scores.pop('Alice')
print(scores, len(scores), scores.keys(), scores.values())

text = """
    Python is a powerful programming language.  
    It is used in data science, web development, automation, and many other field!
    PYTHON is easey to learn, yet very versatile.
"""
text = text.strip().lower()
text = text.replace('!','.')
print(text)
aaa = text.split('\n')
print(aaa)
