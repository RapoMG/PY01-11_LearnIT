"""Problem wyścigu
Napisz program z globalną listą. Stwórz 2 wątki - jeden dodaje do listy 100 tysięcy razy
liczbę 1, a drugi 100 tysięcy razy liczbę 2. Po zakończeniu obu wątków, sprawdź długość
listy. Czy wynosi ona 200 tysięcy? Uruchom program kilka razy.
"""

import threading

list = []

def thread(num):
    for _ in range(1_000_000):
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

"""
100 tysiecy jest za małą próbką, przez co uzyskany wynik w każdej próbie jest identyczny:
200 tysiecy operacji i wątek 2. zaczyna się po zakończeniu wątku 1.
Zwiększenie liczby operacji do 1 mln spowoduje, że rozpoczyna się 'wyścig'.
Dodany licznik pokazuje moment, w którym wątek 2 zaczyna swoje działanie. Przy każdej próbie uzyskujemy
inną wartość licznika.
Lista zawsze ma zadaną długosc 200 tysiecy.
"""