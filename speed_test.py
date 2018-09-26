from block_ai.lib.myblokus.game import Game, GameEnd
from benchmark_game import moves
import argparse
import timeit
import numpy as np

parser = argparse.ArgumentParser(description='Check speed of benchmark game')
parser.add_argument('iterations',  type=int, help='The number of times to run the trial')
args = parser.parse_args()


def time_game():
    g = Game()
    try:
        for move in moves:
            g.make_move(move)
            
    except GameEnd:
        return g


times = [timeit.timeit(stmt=time_game, number=1) for i in range(args.iterations)]
avg_s = np.mean(times)
ms_per_s = 1000
std_dev_ms = np.std(times) * ms_per_s

print("\n==================== Timing Results ====================\n")
print(f"    Total Time: {avg_s:.2} s ± {std_dev_ms:.5} ms for {args.iterations} runs")
print("\n========================== End =========================\n")
