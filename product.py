class Product(object):
	def __init__(self,item_name,price,weight,brand,cost):
		self.item_name = item_name
		self.price = price
		self.weight = weight
		self.brand = brand
		self.cost = cost
		self.status = "for sale"
		return self.display_info()

	def sell(self):
		self.status = "sold"
		print "Status:",self.status
		return self
	def add_tax(self,rate):
		tax_added = self.price * rate
		self.price += tax_added
		print "Price with tax:",self.price
	def return_item(self,reason):
		d = "defective"
		n = "returned in box"
		o = "opened"
		if reason == d:
			self.status = d
			self.price = 0
			print "Status:",self.status
			print "Price:",self.price
		elif reason == n:
			self.status = "for sale"
			print "Status:",self.status
			print "Price:",self.price
		elif reason == o:
			self.status = "Opened and used"
			self.price *= 0.2
			print "Status:",self.status
			print "Price:",self.price
	def display_info(self):
		print "Item Name:",self.item_name
		print "Weight:",self.weight
		print "Brand:",self.brand
		print "Cost:",self.cost
		print "Status:",self.status
		print "Price:",self.price
		self.add_tax(0.09)

# product1 = Product("Banana",10,1,"SunBun",0.30)
