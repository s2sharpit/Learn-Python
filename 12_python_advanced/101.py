# Timing Code Performance
import time

def time_func(func):
    start_time: float = time.perf_counter()

    for i in range(10**5):
        pass

    print("Hello")
    time.sleep(1)

    end_time: float = time.perf_counter()

    # print(f"Time taken: {end_time - start_time:.2f} seconds")
    print(f"Time taken: {end_time - start_time} seconds")


time_func(print)
