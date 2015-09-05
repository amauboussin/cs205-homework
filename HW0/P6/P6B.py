import multiprocessing as mp
import time
import matplotlib.pyplot as plt

# Sleep for t seconds
def burnTime(t):
    time.sleep(t)

# Main
if __name__ == '__main__':
    N = 16  # The number of jobs
    P = 4   # The number of processes

    # A thread pool of P processes
    pool = mp.Pool(P)

    # Use a variety of wait times
    ratio = []
    wait_time = [10 ** -exp for exp in range(7)]

    def time_it(f, args):
        start = time.time()
        f(*args)
        end = time.time()
        return end - start

    for t in wait_time:
        # Compute jobs serially and in parallel
        # Use time.time() to compute the elapsed time for each

        p_start = time.time()
        pool.map(burnTime, [t] * N)
        p_end = time.time()

        s_start = time.time()
        map(burnTime, [t] * N)
        s_end = time.time()

        parallelTime = p_end - p_start
        serialTime = s_end - s_start


        # Compute the ratio of these times
        ratio.append(serialTime/parallelTime)

    # Plot the results
    plt.plot(wait_time, ratio, '-ob')
    plt.xscale('log')
    plt.xlabel('Wait Time (sec)')
    plt.ylabel('Serial Time (sec) / Parallel Time (sec)')
    plt.title('Speedup versus function time')
    plt.show()
