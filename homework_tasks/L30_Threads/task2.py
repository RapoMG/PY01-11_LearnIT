"""Stwórz program, który uruchamia 5 wątków. Każdy wątek powinien otrzymać jako argument
swój numer (od 1 do 5) i wydrukować komunikat "Jestem wątkiem numer [numer]". Upewnij
się, że główny program czeka na zakończenie wszystkich wątków."""

import threading

def thread_task(number):
    print(f"Jestem wątkiem numer {number}")

threads = []

for i in range(1, 6):
    thread = threading.Thread(target=thread_task, args=(i,))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()