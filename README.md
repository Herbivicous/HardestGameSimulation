# HighwayGameSimulation

Will simulate a bunch of games to find the hardest setup possible.

`python main.py 8 10` Will simulate every map of length 8, 10 times.

This simulation can be run in parallel on several cores using MPI

```
mpiexec -n 8 python mpi.py 10 100
```
