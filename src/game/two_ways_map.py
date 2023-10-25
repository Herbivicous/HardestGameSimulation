
from typing import Iterator

from ..model import Checkpoint, Pattern, Card

class TwoWaysMap:

	def __init__(self, checkpoints:list[Checkpoint], last_score:int):
		self.checkpoints = checkpoints
		self.last_score = last_score

	@classmethod
	def from_pattern(cls, pattern:Pattern):

		score = 0
		scores = []

		for case in pattern:

			if case:
				scores.append(score)
				score = 0

			else:
				score += 1

		if scores:
			scores = scores + [2*score] + scores[1:][::-1]

		road = [Checkpoint(None, score) for score in scores]
		last_score = score if not scores else scores[0]

		return cls(road, last_score)

	def fill_checkpoints(self, deck:Iterator[Card]):
		for i in range(len(self.checkpoints)//2):
			self.update_checkpoint(i, next(deck))

	def score(self, index:int) -> int:
		return self.checkpoints[index].score

	def update_checkpoint(self, index:int, card:Card) -> Card:
		current = self.checkpoints[index].card
		self.checkpoints[   index].card = card
		self.checkpoints[-1-index].card = card
		return current

	def __len__(self):
		return len(self.checkpoints)
