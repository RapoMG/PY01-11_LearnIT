"""
Sumowanie z wątkami i blokadą
Napisz program, który sumuje liczby w dużej liście (np. 10 milionów elementów). Podziel
listę na 4 części i każdą część zsumuj w osobnym wątku. Wyniki częściowe dodawaj do
globalnej zmiennej suma_calkowita, zabezpieczając dostęp do niej za pomocą
threading.Lock.
"""

from threading import Lock, Thread
import random

lock = Lock()
suma_calkowita = 0

#huge_list = [1] * 10_000_000
huge_list = [random.randint(1, 10) for _ in range(10_000_000)]

def sum_list(smaller_list):
    global suma_calkowita
    with lock:
        suma_calkowita += sum(smaller_list)

if __name__ == '__main__':

    # no. of parts to split the list
    split_to = 4

    part_length = len(huge_list) // split_to
    parts = [
        huge_list[i * part_length:((i + 1) * part_length if i < split_to - 1 else len(huge_list))] 
        for i in range(split_to)
        ]


    threads = []

    for part in parts:
        thread = Thread(target=sum_list, args=(part,))
        threads.append(thread)
        thread.start()
        

    for thread in threads:
        thread.join()

    print(suma_calkowita)