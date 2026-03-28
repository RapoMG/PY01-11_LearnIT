"""Napisz program, który tworzy i uruchamia jeden wątek. Wątek powinien odczekać 3
sekundy, a następnie wydrukować komunikat "Wątek zakończył pracę!". Główny program
powinien w tym czasie wyświetlić "Główny program czeka na wątek..."."""

import threading
import time

def thread_task():
    time.sleep(3)
    print('Wątek zakończył pracę!')

thread = threading.Thread(target=thread_task)

thread.start()
print("Główny program czeka na wątek...")
thread.join()