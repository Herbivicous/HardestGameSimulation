
from typing import Iterator
from itertools import product

class Pattern:

	def __init__(self, pattern):
		self.pattern = pattern

	@classmethod
	def generate_all_patterns_of_length(cls, length:int) -> Iterator['Pattern']:
		return (cls(p) for p in product((0, 1), repeat=length))

	@classmethod
	def generate_all_patterns_of_length_with_prefix(cls, prefix:tuple[int], length:int) -> Iterator['Pattern']:
		return (cls(prefix + p) for p in product((0, 1), repeat=length))

	def __iter__(self):
		return iter(self.pattern)

	def __eq__(self, other):
		return self.pattern == other.pattern

	def __hash__(self):
		return self.pattern.__hash__()

	def __str__(self):
		return ''.join('x' if c else ' ' for c in self)
