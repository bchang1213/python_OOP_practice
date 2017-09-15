class Animal(object):
	def __init__(self,name,health):
		self.name = name
		self.health = health
	def walk(self):
		self.health -= 1
	def run(self):
		self.health -= 5
	def display_health(self):
		print self.health

# LET THERE BE ANIMAL 1
animal1 = Animal("Jerry",15)

animal1.walk()
animal1.walk()
animal1.walk()

animal1.run()
animal1.run()

animal1.display_health()


class Dog(Animal):
	def __init__(self,name,health):
		super(Dog, self).__init__(name,health)
		self.health = 150
	def pet(self):
		self.health += 5

#LET THERE BE A DOGE
dog1 = Dog("Blue", 3)
dog1.walk()
dog1.walk()
dog1.walk()

dog1.run()
dog1.run()

dog1.pet()

dog1.display_health()

class Dragon(Animal):
	def __init__(self,name,health):
		super(Dragon,self).__init__(name,health)
		self.health = 170
	def fly(self):
		self.health -= 10
	def display_health(self):
		super(Dragon,self).display_health()
		print "I am a Dragon"

#Rock the Dragon

ballz = Dragon("Goku", 100)
ballz.fly()
ballz.display_health()