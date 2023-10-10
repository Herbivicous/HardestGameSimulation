
from ..model import Card
from . import Map

class Game:

	def __init__(self, game_map:Map):

		self.game_map = game_map

		self.position = 0

	@property
	def is_over(self) -> bool:
		return self.position == len(self.game_map)

	def update_checkpoint(self, card:Card) -> Card:
		return self.game_map.update_checkpoint(self.position, card)

	def move_forward(self) -> int:
		score = self.game_map.score(self.position)
		self.position += 1
		return score

	def move_backward(self) -> int:
		score = self.game_map.score(self.position)
		self.position = max(0, self.position - 1)

		if score:
			return score

		if self.position == 0:
			return 1

		return 0

	@property
	def last_score(self) -> int:
		return self.game_map.last_score
