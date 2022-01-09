
from typing import List

from ..model import Checkpoint, Pattern, Card
from . import Deck

class OneWayMap:

	def __init__(self, checkpoints:List[Checkpoint], last_score:int):
		self.checkpoints = checkpoints
		self.last_score = last_score

	@classmethod
	def from_pattern(cls, pattern:Pattern):

		res, score = [], 0

		for case in pattern:

			if case:
				res.append(Checkpoint(None, score))
				score = 0

			else:
				score += 1

		return cls(res, score)

	def fill_checkpoints(self, deck:Deck):
		for checkpoint in self.checkpoints:
			checkpoint.card = deck.draw_card()

	def score(self, index:int) -> int:
		return self.checkpoints[index].score

	def update_checkpoint(self, index:int, card:Card) -> Card:
		current = self.checkpoints[index].card
		self.checkpoints[index].card = card
		return current

	def __len__(self):
		return len(self.checkpoints)
