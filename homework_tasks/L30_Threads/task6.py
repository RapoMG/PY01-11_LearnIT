"""
Pierwszy proces
Napisz program, który uruchamia osobny proces. Proces ten powinien obliczyć silnię liczby
10 i wydrukować wynik.
"""

import multiprocessing
from math import factorial

def silnia(n):
    print(factorial(n))

if __name__ == '__main__':
    process = multiprocessing.Process(target=silnia, args=(10,))
    process.start()
    process.join()

