
from typing import Protocol

from ..model import Checkpoint, Pattern, Card
from . import Deck

class Map(Protocol):

	@property
	def last_score(self) -> int:
		...

	@classmethod
	def from_pattern(cls, pattern:Pattern):
		...

	def fill_checkpoints(self, deck:Deck):
		...

	def score(self, index:int) -> int:
		...

	def update_checkpoint(self, index:int, card:Card) -> Card:
		...

	def __len__(self):
		...
