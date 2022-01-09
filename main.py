
import sys
from argparse import ArgumentParser

from src.game_runner import GameRunner
from src.game import Deck, OneWayMap, TwoWaysMap
from src.model import Pattern
from src.simulation.strategies import UserInput, Random, NaiveAI
from src.simulation import run_simulation

def main(args):

	patterns = list(Pattern.generate_all_patterns(args.length))

	maps = {p: TwoWaysMap.from_pattern(p) for p in patterns}
	scores = {p: 0 for p in patterns}

	runner = GameRunner(NaiveAI())

	base_deck = Deck.new_52_cards_deck()

	scores = run_simulation(runner, args.trials, base_deck, maps)

	return {p: s/args.trials for p, s in sorted(scores.items(), key=lambda e:e[1])}

if __name__ == '__main__':
	
	parser = ArgumentParser()
	parser.add_argument(dest='length', type=int)
	parser.add_argument(dest='trials', type=int)

	result = main(parser.parse_args())

	print('\n'.join(f'{p}:{s}' for p, s in result.items()))
