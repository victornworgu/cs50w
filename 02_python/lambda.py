"""
square = lambda x: x * x

def square(x):
	return x * x
"""

people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def j(person):
    return person["name"]

people.sort(key=j)

print(people)
