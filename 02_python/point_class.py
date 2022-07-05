class Point():
	def __init__(self, x, y):
		self.h = x
		self.w = y

p = Point(input("Enter Pont 1: "), input("Enter Point 2: "))
print(f"{p.h}, {p.w}")
