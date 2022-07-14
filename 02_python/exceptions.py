"""x = int(input("x: "))
y = int(input("y: "))

result = x / y

print(f"{x} / {y} = {result}")"""

import sys

"""x = int(input("x: "))
y = int(input("y: "))

try:
	result = x / y
except ZeroDivisionError:
	print("Error: Cannot divide by 0.")
	sys.exit(1)

print(f"{x} / {y} = {result}")"""

try:
	x = int(input("x: "))
	y = int(input("y: "))
except ValueError:
	print("Error: Your input should contain whole numbers only.")
	sys.exit(1)

try:
	result = x / y
except ZeroDivisionError:
	print("Error: Cannot divide by 0.")
	sys.exit(1)

print(f"{x} / {y} = {result}")
