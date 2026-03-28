'''
Pula procesów do przetwarzania danych
Stwórz listę 100 losowych liczb od 1 do 1000. Użyj multiprocessing.Pool do stworzenia puli
procesów, która dla każdej liczby sprawdzi, czy jest ona liczbą pierwszą. Funkcja pool.map
powinna zwrócić listę wartości True/False. Wydrukuj, ile liczb pierwszych znalazłeś
'''

import random
import multiprocessing

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [random.randint(1, 1000) for _ in range(100)]

if __name__ == "__main__":
    results = []
    with multiprocessing.Pool() as pool:
        results = pool.map(is_prime, numbers)

    
    print(f"Number of prime numbers: {sum(results)}")
    
