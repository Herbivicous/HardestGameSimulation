
from typing import Iterator

from ..model import Checkpoint, Pattern, Card

class OneWayMap:

	def __init__(self, checkpoints:list[Checkpoint], last_score:int):
		self.checkpoints = checkpoints
		self.last_score = last_score

	@classmethod
	def from_pattern(cls, pattern:Pattern):

		res, score = list[Checkpoint](), 0

		for case in pattern:

			if case:
				res.append(Checkpoint(None, score))
				score = 0

			else:
				score += 1

		return cls(res, score)

	def fill_checkpoints(self, deck: Iterator[Card]):
		for checkpoint in self.checkpoints:
			checkpoint.card = next(deck)

	def score(self, index:int) -> int:
		return self.checkpoints[index].score

	def update_checkpoint(self, index:int, card:Card) -> Card:
		current = self.checkpoints[index].card
		self.checkpoints[index].card = card
		return current

	def __len__(self):
		return len(self.checkpoints)
