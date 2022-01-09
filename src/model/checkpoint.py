
from dataclasses import dataclass
from typing import Optional

from . import Card

@dataclass
class Checkpoint:
	card:Card
	score:int
