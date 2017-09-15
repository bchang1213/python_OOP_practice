class car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price

		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
			self.tax

		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.display_all()
	def display_all(self):
		print "Price:",self.price,"dollars."
		print "Speed:",self.speed,"miles per hour."
		print "Fuel Status:",self.fuel
		print "Mileage:",self.mileage,"miles to the gallon."
		print "Tax:",self.tax
		return self
	def __str__(self):
		return "I am a car"


car1 = car(10000,50,"Full",20000)

print car1