
from typing import Protocol, Iterator

from ..model import Pattern, Card

class Map(Protocol):

	@property
	def last_score(self) -> int:
		...

	@classmethod
	def from_pattern(cls, pattern:Pattern):
		...

	def fill_checkpoints(self, deck: Iterator[Card]):
		...

	def score(self, index:int) -> int:
		...

	def update_checkpoint(self, index:int, card:Card) -> Card:
		...

	def __len__(self):
		...
