class ElementEfremova():
	def __init__(self, name, symbol, number):
                self.name = name
                self.symbol = symbol
                self.number = number
	
	def dump():
		print('name:', self.name)
		print('symbol:', self.symbol)
		print('number:', self.number)

element = ElementEfremova('Бор', 'B', 5)
element.dump