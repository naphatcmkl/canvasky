# Multithreading

import multiprocessing as mp
import numpy as np
import time


def test(i, param1, param2, param3):
    result = param1 ** 2 * param2 + param3
    time.sleep(2)

    return (i, result)


def results_get(result):
    global results
    results.append(result)


if __name__ == '__main__':
    params = np.random.random((10, 3)) * 100
    results = []
    print('Number of CPUs available:', mp.cpu_count())
    ts = time.time()
    pool = mp.Pool(4)
    for i in range(0, params.shape[0]):
        # results_get(test(i, params[i, 0], params[i, 1], params[i, 2]))
        pool.apply_async(test, args=(i, params[i, 0], params[i, 1], params[i, 2]), callback=results_get)
    pool.close()
    pool.join()
    print('Time:', time.time() - ts)

    print(results)
