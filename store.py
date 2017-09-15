from product import Product

class Store(object):
	def __init__(self):
		self.products = []
		self.location = "Burbank, CA"
		self.owner = "owner"
	def add_product(self,productname):
		self.products.append(productname)
		return self.products
	def remove_product(self,productname):
		for i in range(0,len(self.products)):
			if productname == self.products[i]:
				self.products.pop(i)
		return self.products
	def inventory(self):
		print "Inventory:"
		print "\n"
		for v in range(0,len(self.products)):
			self.products[v].display_info()

print "Product 1"
product1 = Product("Banana",10,1,"SunBun",0.30)

print "\n"

print "Product 2"
product2 = Product("Cup",5,1,"Cuppers",0.40)

print "\n"

print "Store1"
store1 = Store()
store1.add_product(product1)

store1.inventory()