class Flight():
	def __init__(self,cap):
		self.capacity = cap
		self.passengers = []

	def open_seats(self):
		return self.capacity - len(self.passengers)

	def add_passenger(self, name):
		if not self.open_seats():
			return False
		self.passengers.append(name)
		return True

flight = Flight(3)
print("///////////////////////WELCOME TO NVC AIRLINES//////////////////////////")

# using For Loop
people = []
for person in range(flight.capacity+1):
	people.append(input("Enter Name of Passenger: "))
	if flight.add_passenger(people[person]):
		print(f"{people[person]} has been booked successfully")
		#print(f"{person} {people[person]} {people}")
print(f"Sorry, flight full. No seat for {people[person]}")



"""# using While Loop
person = []
while len(person) <= flight.capacity:
	person.append(input("Enter Name of Passenger: "))
	if flight.add_passenger(person):
		print(f"{person[len(person)-1]} has been booked successfully")
		#print(len(person))
	#elif not flight.add_passenger(person):
print(f"Sorry, flight full. No seat for {person[len(person)-1]}")
"""
