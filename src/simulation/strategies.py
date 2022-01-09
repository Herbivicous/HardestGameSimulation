
from random import choice

from ..model import Card
from ..game_runner import StrategyChoice


class UserInput:

	choice_map = {
		'+': StrategyChoice.higher,
		'-': StrategyChoice.lower,
		'=': StrategyChoice.equal
	}

	def get_choice(self, card:Card) -> StrategyChoice:
		return self.choice_map[input(f'{card} (+, -, =) ?')]


class Random:

	def get_choice(self, card:Card) -> StrategyChoice:
		return choice((StrategyChoice.higher, StrategyChoice.lower))


class NaiveAI:

	def get_choice(self, card:Card) -> StrategyChoice:
		return StrategyChoice.higher if card.value_i < 7 else StrategyChoice.lower
