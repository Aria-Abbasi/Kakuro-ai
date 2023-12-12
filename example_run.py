import numpy as np
import time
from kakuro_optimized import Kakuro as KakuroOptimized
from kakuro_standard import Kakuro

def create_field(difficulty):
    if difficulty == 'easy':
        return np.array([
            [Kakuro.WALL, Kakuro.WALL, Kakuro.set_targets(top=30), Kakuro.set_targets(top=4), Kakuro.set_targets(top=24), Kakuro.WALL, Kakuro.set_targets(top=4), Kakuro.set_targets(top=16),],
            [Kakuro.WALL, Kakuro.set_targets(left=19, top=16), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(left=10, top=9), Kakuro.EMPTY, Kakuro.EMPTY,],
            [Kakuro.set_targets(left=39), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY,],
            [Kakuro.set_targets(left=15), Kakuro.EMPTY, Kakuro.EMPTY,  Kakuro.set_targets(left=10, top=23), Kakuro.EMPTY, Kakuro.EMPTY,  Kakuro.set_targets(top=10), Kakuro.WALL,],
            [Kakuro.WALL, Kakuro.set_targets(left=16), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(left=4, top=6), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(top=16),],
            [Kakuro.WALL, Kakuro.set_targets(top=14), Kakuro.set_targets(top=16,left=9), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(top=4, left=12), Kakuro.EMPTY, Kakuro.EMPTY,],
            [Kakuro.set_targets(left=35), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY,],
            [Kakuro.set_targets(left=16), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(left=7), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.WALL,],
        ])
    elif difficulty == 'medium':
        return np.array([
            [Kakuro.WALL, Kakuro.WALL, Kakuro.set_targets(top=20), Kakuro.set_targets(top=3), Kakuro.set_targets(top=23), Kakuro.WALL, Kakuro.set_targets(top=12), Kakuro.set_targets(top=16)],
            [Kakuro.WALL, Kakuro.set_targets(left=12, top=5), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(left=16, top=24), Kakuro.EMPTY, Kakuro.EMPTY],
            [Kakuro.set_targets(left=41), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY],
            [Kakuro.set_targets(left=3), Kakuro.EMPTY, Kakuro.EMPTY , Kakuro.set_targets(left=13, top=24), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(top=11), Kakuro.WALL],
            [Kakuro.WALL, Kakuro.set_targets(left=17), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(left=10, top=23), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(top=16)],
            [Kakuro.WALL, Kakuro.set_targets(top=14), Kakuro.set_targets(left=16, top=5), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(left=11, top=17), Kakuro.EMPTY, Kakuro.EMPTY],
            [Kakuro.set_targets(left=42), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY],
            [Kakuro.set_targets(left=10), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(left=22) ,Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.WALL],
        ])
    elif difficulty == 'hard':
        return np.array([
            [Kakuro.WALL, Kakuro.set_targets(top=10), Kakuro.set_targets(top=10), Kakuro.WALL, Kakuro.WALL, Kakuro.WALL, Kakuro.WALL, Kakuro.WALL, Kakuro.set_targets(top=23), Kakuro.set_targets(top=16)],
            [Kakuro.set_targets(left=4), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(top=17), Kakuro.WALL, Kakuro.WALL, Kakuro.WALL, Kakuro.set_targets(left=16, top=17), Kakuro.EMPTY, Kakuro.EMPTY],
            [Kakuro.set_targets(left=23), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(top=20), Kakuro.WALL, Kakuro.set_targets(left=24, top= 30), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY],
            [Kakuro.WALL, Kakuro.set_targets(left=13), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(left=23, top=20), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.WALL],
            [Kakuro.WALL, Kakuro.WALL, Kakuro.WALL, Kakuro.set_targets(left=11), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.WALL, Kakuro.WALL],
            [Kakuro.WALL, Kakuro.WALL, Kakuro.WALL, Kakuro.set_targets(left=23, top=6), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.WALL, Kakuro.WALL, Kakuro.WALL],
            [Kakuro.WALL, Kakuro.WALL, Kakuro.set_targets(left=25, top=7), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(top=3), Kakuro.set_targets(top=9), Kakuro.WALL],
            [Kakuro.WALL, Kakuro.set_targets(left=8, top=4), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(left=7), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(top=4)],
            [Kakuro.set_targets(left=6), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.WALL, Kakuro.WALL, Kakuro.set_targets(left=6), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY],
            [Kakuro.set_targets(left=3), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.WALL, Kakuro.WALL, Kakuro.WALL, Kakuro.WALL, Kakuro.set_targets(left=4), Kakuro.EMPTY, Kakuro.EMPTY],
        ])
    elif difficulty == 'expert':
        return  np.array([
            [Kakuro.WALL, Kakuro.WALL, Kakuro.WALL, Kakuro.set_targets(top=17), Kakuro.set_targets(top=19), Kakuro.WALL, Kakuro.WALL, Kakuro.set_targets(top=7), Kakuro.set_targets(top=44), Kakuro.WALL],
            [Kakuro.WALL, Kakuro.set_targets(top=3), Kakuro.set_targets(top=37, left=17), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.WALL, Kakuro.set_targets(left=10), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(top=23)],
            [Kakuro.set_targets(left=20), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(top=6), Kakuro.set_targets(top=3, left=15), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY],
            [Kakuro.set_targets(left=5), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(left=25, top=3), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY],
            [Kakuro.WALL, Kakuro.set_targets(left=8), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(left=3), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(left=15,top=10), Kakuro.EMPTY, Kakuro.EMPTY],
            [Kakuro.WALL, Kakuro.set_targets(left=3, top=13), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(top=7), Kakuro.set_targets(top=5), Kakuro.set_targets(left=17), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.WALL],
            [Kakuro.set_targets(left=9), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(left=3, top=10), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(left=6,top=16), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(top=11)],
            [Kakuro.set_targets(left=38), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.set_targets(left=17, top=3), Kakuro.EMPTY, Kakuro.EMPTY],
            [Kakuro.set_targets(left=7), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.WALL, Kakuro.set_targets(left=12), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.EMPTY],
            [Kakuro.WALL, Kakuro.set_targets(left=4), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.WALL, Kakuro.set_targets(left=3), Kakuro.EMPTY, Kakuro.EMPTY, Kakuro.WALL, Kakuro.WALL]
        ])

def solve_and_measure(difficulty):
    field = create_field(difficulty)
    game = Kakuro(field)
    field = create_field(difficulty)
    gameOptimized = KakuroOptimized(field)

    start_time = time.time()
    game.solve()
    standard_time = time.time() - start_time

    start_time = time.time()
    gameOptimized.solve()
    optimized_time = time.time() - start_time

    return standard_time, optimized_time

for difficulty in ['easy', 'medium', 'hard', 'expert']:
    standard_time, optimized_time = solve_and_measure(difficulty)
    print(f"{difficulty.title()} Difficulty:")
    print(f"Standard Kakuro: {standard_time:.4f} seconds")
    print(f"Optimized Kakuro: {optimized_time:.4f} seconds")
    print("----------")
