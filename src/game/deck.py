
from typing import List, Optional
from random import shuffle

from ..model import Card, VALUE, COLOR

class Deck:

	def __init__(self, cards:List[Card]):
		self.cards = cards
		self.index = 0

	@classmethod
	def new_52_cards_deck(cls):
		return cls(
			[
				Card(value, color)
				for value in range(len(VALUE))
				for color in range(len(COLOR))
			]
		)

	@classmethod
	def copy(cls, deck:'Deck') -> 'Deck':
		return cls(deck.cards)

	def shuffle(self):
		shuffle(self.cards)
		return self

	def draw_card(self) -> Optional[Card]:
		try:
			self.index += 1
			return self.cards[self.index - 1]

		except IndexError:
			return None
