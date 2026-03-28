"""Symulacja pobierania danych
Napisz funkcję pobierz_dane(id_danych), która symuluje pobieranie danych przez
time.sleep(2). Uruchom tę funkcję dla 3 różnych id_danych sekwencyjnie i zmierz czas.
Następnie zrób to samo, ale uruchamiając każdą funkcję w osobnym wątku i również
zmierz czas. Porównaj wyniki."""

import threading
import time


def pobierz_dane(id_danych):
    time.sleep(2)
    return id_danych

start_time = time.time()

for i in range(1, 4):    
    print(pobierz_dane(i))

print(f"Sekwencyjnie. Czas wykonania: {time.time() - start_time}")

threads = []

for i in range(1, 4):
    thread = threading.Thread(target=pobierz_dane, args=(i,))
    threads.append(thread)

start_time = time.time()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Wątki. Czas wykonania: {time.time() - start_time}")

"""Wynik obu metod różni się o tysięczne części sekundy (pomijając czas uśpienia funcji).
Program napisany na zajęciach zaokrąglął czas do 2. cyfry po przecinku.
"""
