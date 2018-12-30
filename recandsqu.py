class Shape:
	def __init__(self, l, w):
		self.length = l
		self.width = w

	def what_am_i(self):
		print("I am a shape")

class Rectangle(Shape):

	def calculate_perimeter(self, length, width):
		return 2*length + 2*width


class Square(Shape):
	square_list = []
	square_list.append("{} by {} by {} by {}".format(length, length, length, length))

	def calculate_perimeter(self, length):
		return 4 * length

	def change_size(self, change):
		self.length = self.length + change




rec1 = Rectangle(4, 5)
squ1 = Square(5,5)

print(rec1.calculate_perimeter(4,5))
print(squ1.calculate_perimeter(5))

change1 = float(input("How much change? "))

squ1.change_size(change1)

print(squ1.length)
print(squ1.calculate_perimeter(squ1.length))

squ1.what_am_i()
rec1.what_am_i()

print(Square.square_list)