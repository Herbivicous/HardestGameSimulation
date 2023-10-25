
import sys
import math

from mpi4py import MPI  # type: ignore[import]

from src.game_runner import GameRunner
from src.game import Deck, OneWayMap, TwoWaysMap
from src.model import Pattern
from src.simulation import strategies
from src.simulation import run_simulation

comm = MPI.COMM_WORLD
rank, size = comm.Get_rank(), comm.Get_size()

if len(sys.argv) < 3:
	print('Missing parameters: python <map_length> <nb_of_runs>')
	sys.exit(1)

map_length = int(sys.argv[1])
nb_of_runs = int(sys.argv[2])

base = int(math.log2(size))

prefix = tuple(int(c != '0') for c in format(rank, f'0{base}b'))
patterns = list(Pattern.generate_all_patterns_of_length_with_prefix(prefix, map_length - base))

maps = {p: TwoWaysMap.from_pattern(p) for p in patterns}
scores = {p: 0 for p in patterns}

runner = GameRunner(strategies.NaiveAI())

base_deck = Deck.new_52_cards_deck()

scores = run_simulation(runner, nb_of_runs, base_deck, maps)

gathered_scores = comm.gather(scores, root=0)

if rank == 0:
	scores = {k:v for sublist in gathered_scores for k, v in sublist.items()}
	print('\n'.join(f"{p}:{s/nb_of_runs}" for p, s in sorted(scores.items(), key=lambda e:e[1])))
