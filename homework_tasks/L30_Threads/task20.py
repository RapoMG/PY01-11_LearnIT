"""
AI: Równoległe przetwarzanie obrazów (symulacja)
Załóżmy, że masz do przetworzenia 10 "obrazów", reprezentowanych jako listy 1000x1000
losowych liczb. Napisz funkcję zastosuj_filtr(obraz), która iteruje po każdym "pikselu" i
wykonuje na nim jakąś operację matematyczną (np. piksel * 1.1), symulując zadanie CPUbound.
Użyj multiprocessing.Pool do przetworzenia wszystkich 10 obrazów równolegle i zmierz
czas. Porównaj go z czasem wykonania sekwencyjnego.
"""
from random import randint
from multiprocessing import Pool
from time import time

#list with 1000x1000 random numbers
pictures = [
    [
        [randint(0,256) for _ in range(1000)] for _ in range(1000)
    ] for _ in range(10)
]

def zastosuj_filtr(picture):
    return [[pixel * 1.1 for pixel in row] for row in picture]


if __name__ == "__main__":
    start_time = time()

    with Pool() as pool:
        result = pool.map(zastosuj_filtr, pictures)
    print(f"Multiprocessing. Czas wykonania: {time() - start_time}")

    start_time = time()

    result = [zastosuj_filtr(picture) for picture in pictures]
    print(f"Sekwencyjnie. Czas wykonania: {time() - start_time}")
