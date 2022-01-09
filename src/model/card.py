
from dataclasses import dataclass

COLOR = ['♥', '♦', '♠', '♣']
VALUE = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'D', 'K']

@dataclass
class Card:

	value_i:int
	color_i:int

	@property
	def value(self):
		return VALUE[self.value_i]

	@property
	def color(self):
		return COLOR[self.color_i]

	def __eq__(self, other):
		return self.value_i == other.value_i

	def __lt__(self, other):
		return self.value_i < other.value_i

	def __gt__(self, other):
		return self.value_i > other.value_i

	def __str__(self):
		return f'{self.value}{self.color}'
