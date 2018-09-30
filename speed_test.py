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
std_dev = np.std(times)

def get_time_string(time):

    metric_conversion = 1000
     
    if time < 1.0:
        unit = "ms"
        time *= metric_conversion

    if time < 1.0:
        unit = "ns"
        time *= metric_conversion

    return f"{time:.2f} {unit}"

    
    
   
        
        

print("\n==================== Timing Results ====================\n")
print(f"    Total Time: {get_time_string(avg_s)} ± {get_time_string(std_dev)} for {args.iterations} runs")
print("\n========================== End =========================\n")
