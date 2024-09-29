import time
import numpy as np

def test_performance():
    sizes = [10**3, 10**4, 10**5]
    for size in sizes:
        arr = list(np.random.randint(0, 100000, size))
        k = size // 2
        
        # Test deterministic algorithm
        start = time.time()
        median_of_medians(arr.copy(), k)
        end = time.time()
        print(f"Deterministic (Median of Medians) for size {size}: {end - start} seconds")
        
        # Test randomized algorithm
        start = time.time()
        randomized_select(arr.copy(), 0, len(arr)-1, k)
        end = time.time()
        print(f"Randomized Quickselect for size {size}: {end - start} seconds")
        
test_performance()
