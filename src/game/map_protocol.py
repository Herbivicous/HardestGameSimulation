
from typing import Protocol

from ..model import Pattern, Card
from .deck import DeckIterator

class Map(Protocol):

	@property
	def last_score(self) -> int:
		...

	@classmethod
	def from_pattern(cls, pattern:Pattern):
		...

	def fill_checkpoints(self, deck:DeckIterator):
		...

	def score(self, index:int) -> int:
		...

	def update_checkpoint(self, index:int, card:Card) -> Card:
		...

	def __len__(self):
		...
