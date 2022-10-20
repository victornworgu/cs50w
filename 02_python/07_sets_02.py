# create an empty set
s = set()

# add elements to set
s.add(input("Enter element: "))
s.add(input("Enter element: "))
s.add(input("Enter element: "))
a = input("Do you want to add more? y/n: ")
if a == "n":
	print(f"Set has {len(s)} elements")
	ad = input("Do you want to display the elements? y/n: ")
	if ad == "y":
		print(s)
#s.add(2)
#s.add(3)
#s.add(4)
#print(s)
