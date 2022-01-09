
from ..game import Game, OneWayMap, Deck
from . import GameStrategy, StrategyChoice

class GameRunner:

	def __init__(self, strategy:GameStrategy):
		self.strategy = strategy

	def play(self, game:Game, deck:Deck, do_print:bool=False) -> int:

		score = 0

		while not game.is_over:

			card = deck.draw_card()

			if not card:
				return score

			checkpoint_card = game.update_checkpoint(card)
			choice = self.strategy.get_choice(checkpoint_card)

			if (
				choice == StrategyChoice.lower and checkpoint_card > card or
				choice == StrategyChoice.higher and checkpoint_card < card or
				choice == StrategyChoice.equal and checkpoint_card == card
			):
				score += game.move_forward()
			else:
				score += game.move_backward()

		return score + game.last_score
