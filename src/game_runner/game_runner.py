
from typing import Iterator

from ..game import Game
from ..model import Card
from . import GameStrategy, StrategyChoice

class GameRunner:

	def __init__(self, strategy:GameStrategy):
		self.strategy = strategy

	def play(self, game:Game, deck: Iterator[Card]) -> int:

		score = 0

		while not game.is_over:

			card = next(deck, None)

			if not card:
				return score

			checkpoint_card = game.update_checkpoint(card)
			choice = self.strategy.get_choice(checkpoint_card)

			if any((
				choice == StrategyChoice.lower and checkpoint_card > card,
				choice == StrategyChoice.higher and checkpoint_card < card,
				choice == StrategyChoice.equal and checkpoint_card == card
			)):
				score += game.move_forward()
			else:
				score += game.move_backward()

		return score + game.last_score
