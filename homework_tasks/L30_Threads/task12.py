'''
GIL w praktyce (CPU-bound)
Napisz funkcję, która wykonuje intensywne obliczenia, np. sum(i*i for i in
range(20_000_000)). Zmierz czas wykonania tej funkcji dwa razy pod rząd. Następnie
zmierz czas wykonania jej dwa razy jednocześnie w dwóch różnych wątkach. Na koniec
zmierz czas, wykonując ją dwa razy jednocześnie w dwóch różnych procesach. Porównaj i
wyjaśnij wyniki w komentarzu w kodzie.
'''

from threading import Thread
from multiprocessing import Process
from time import time

def heavy_work():
    sum(i*i for i in range(20_000_000))


if __name__ == "__main__":
    
    # single thread
    start_time = time()

    heavy_work()
    heavy_work()

    print(f"Single thread time: {time() - start_time}")

    # two threads
    start_time = time()

    t1 = Thread(target=heavy_work)
    t2 = Thread(target=heavy_work)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(f"Two threads time: {time() - start_time}")

    # two processes
    start_time = time()

    p1 = Process(target=heavy_work)
    p2 = Process(target=heavy_work)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"Two processes time: {time() - start_time}")

    """
    Single thread with two tasks means that second task is executed after first has finished everything.
    Two threads for two tasks means that tasks still are executed one after another, arranged by GIL. That makes time diffirence almost nonexistent.
    Two processes for two tasks means that both tasks are executed in parallel, bound by avilable CPU cores. That makes them much faster.
    """