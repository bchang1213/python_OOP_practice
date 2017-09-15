class bike(object):
	def __init__(self,price,max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print "This bike's price is",self.price,"dollars."
		print "This bike's max speed is",self.max_speed,"per hour."
		print "This bike has",self.miles,"miles traveled."
		return self
	def ride(self):
		print "Riding..."
		self.miles += 10
		return self
	def reverse(self):
		if self.miles >= 5:
			print "Reversing..."
			self.miles -= 5
			return self
		else:
			print "You cannot reverse, you must travel forward first."


bike1 = bike(300,50)
print "bike1"
bike1.ride()
bike1.ride()
bike1.ride()
print bike1.displayInfo()

bike2 = bike(0,10)
print "bike2"
bike2.ride()
bike2.ride()
print bike2.displayInfo()
bike2.reverse()
bike2.reverse()
print bike2.displayInfo()

bike3 = bike(10,10)
print "bike3"
bike3.reverse()
bike3.reverse()
bike3.reverse()
print bike3.displayInfo()
