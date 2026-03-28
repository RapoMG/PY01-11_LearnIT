"""
Naprawa wyścigu
Zmodyfikuj program z zadania 4, dodając threading.Lock, aby operacja dodawania do listy
była bezpieczna. Sprawdź, czy teraz długość listy jest zawsze poprawna.
"""

import threading

list = []
lock = threading.Lock()

def thread(num):
    for _ in range(1_000_000):
        with lock:
            list.append(num)

thread1 = threading.Thread(target=thread, args=(1,))
thread2 = threading.Thread(target=thread, args=(2,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(len(list))

counter = 0
for n in list:
    if n == 1:
        counter += 1
    else:
        break

print(counter)