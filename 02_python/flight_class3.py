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
for p in range(flight.capacity+1):
	nom = (input("Enter Name of Passenger: "))
	if flight.add_passenger(nom):
		print(f"{flight.passengers[p]} has been booked successfully")
		#print(f"{p} {flight.passengers[p]} {flight.passengers}")
print(f"Sorry, flight full booked. No available seat for {nom}")
