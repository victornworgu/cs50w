class Flight():
	def __init__(self,cap):
		self.capacity = cap
		self.passengers = []

	def open_seats(self):
		return self.capacity - len(self.passengers)

	def add_passenger(self, nom):
		if not self.open_seats():
			return False
		self.passengers.append(nom)
		return True

flight = Flight(3)
print("///////////////////////WELCOME TO NVC AIRLINES//////////////////////////")

# using For Loop
for p in range(flight.capacity):
	nom = (input("Enter Name of Passenger: "))
	if flight.add_passenger(nom):
		print(f"{flight.passengers[p]} has been booked successfully.")
print(f"Booking for Flight 775 Closed. All {flight.capacity} seats has been booked.")
