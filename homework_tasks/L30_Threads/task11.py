"""
Producent i konsument
Zaimplementuj klasyczny problem producenta-konsumenta. Stwórz współdzieloną,
bezpieczną wątkowo kolejkę (import queue; q = queue.Queue()). "Producent" to wątek,
który co sekundę dodaje do kolejki nowy element (np. losową liczbę). "Konsument" to
wątek, który co 1.5 sekundy pobiera element z kolejki i go drukuje. Program powinien
działać przez 10 sekund.
"""

from queue import Queue
from random import randint
from threading import Thread
from time import sleep, time


q = Queue() 

def producer(start: int, stop: int):
    while time() - start < stop:
        q.put(randint(1, 10))
        sleep(1)

def consumer(start: int, stop: int):
    while time() - start < stop:
        print(q.get())
        sleep(1.5)

if __name__ == "__main__":
    work_time = 10
    start = time()

    producer_thread = Thread(target=producer, args=(start, work_time,))
    consumer_thread = Thread(target=consumer, args=(start, work_time,))
   
    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()
    

    print(F"Finished in {(time() - start):.4f} seconds")
