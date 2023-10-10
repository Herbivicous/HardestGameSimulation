
from enum import Enum
from typing import Protocol

from ..model import Card

class StrategyChoice(Enum):
	higher = 0
	lower = 1
	equal = 2

class GameStrategy(Protocol):

	def get_choice(self, card:Card) -> StrategyChoice:
		...
