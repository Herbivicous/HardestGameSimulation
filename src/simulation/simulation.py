
from ..game import Deck, Game

def run_simulation(runner, runs, base_deck, maps):

	scores = {p: 0 for p in maps}

	for _ in range(runs):

		base_deck.shuffle()

		for pattern, pattern_map in maps.items():

			deck = base_deck.copy(base_deck)

			pattern_map.fill_checkpoints(deck)

			autoroute = Game(pattern_map, deck)

			scores[pattern] += runner.play(autoroute, deck)

	return scores
