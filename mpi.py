
import sys
from itertools import count, takewhile
from mpi4py import MPI
import math

from src.game_runner import GameRunner
from src.game import Deck, OneWayMap, TwoWaysMap
from src.model import Pattern
from src.simulation.strategies import UserInput, Random, NaiveAI
from src.simulation import run_simulation

comm = MPI.COMM_WORLD
rank, size = comm.Get_rank(), comm.Get_size()

P = int(sys.argv[1])
N = int(sys.argv[2])

base = next((i for i in takewhile(lambda i: i <= size, count()) if 2**i == size), None)
assert base, 'Size must be a power of 2'


prefix = tuple(c != '0' for c in format(rank, f'0{base}b'))
patterns = list(Pattern.generate_all_patterns_with_prefix(prefix, P - base))

maps = {p: TwoWaysMap.from_pattern(p) for p in patterns}
scores = {p: 0 for p in patterns}

runner = GameRunner(NaiveAI())

base_deck = Deck.create_52_cards_deck()

scores = run_simulation(runner, N, base_deck, maps)

scores = comm.gather(scores, root=0)

if rank == 0:

	scores = {k:v for sublist in scores for k, v in sublist.items()}
	print('\n'.join(f"{p}:{s/N}" for p, s in sorted(scores.items(), key=lambda e:e[1])))

