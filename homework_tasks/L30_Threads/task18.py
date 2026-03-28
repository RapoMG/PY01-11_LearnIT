'''
Symulacja wyścigu w banku
Stwórz klasę KontoBankowe z atrybutem saldo. Stwórz metody wplac(kwota) i wyplac(kwota).
Metoda wyplac powinna sprawdzać, czy na koncie jest wystarczająco środków. Uruchom 10
wątków, z których 5 wpłaca losowe kwoty, a 5 wypłaca losowe kwoty. Zabezpiecz metody za
pomocą blokady, aby saldo na koniec było prawidłowe.
'''

from threading import Lock,Thread
import random
from colorama import Fore, init

init()


class KontoBankowe:
    def __init__(self):
        self.__saldo = 0
        self._lock = Lock()

    def wplac(self, kwota):
        with self._lock:
            if kwota < 0:
                return
            self.__saldo += kwota

    def wyplac(self, kwota):
        with self._lock:
            if self.__saldo >= kwota:
                self.__saldo -= kwota
                return True
            return False

    def get_saldo(self):
        with self._lock:
            return self.__saldo


def worker_deposit(account):
    for _ in range(100):  # for more racy results
        amont = random.randint(1, 100)
        account.wplac(amont)
        print(Fore.GREEN + f"Wplata udana: {amont}")

def worker_withdrawal(account):
    for _ in range(100):  # for more racy results
        amont = random.randint(1, 100)
        success = account.wyplac(amont)

        if success:
            print(Fore.YELLOW + f"Wyplata udana: {amont}")
        else:
            print(Fore.RED + f"Wyplata nieudana: {amont}")


if __name__ == "__main__":
    account = KontoBankowe()

    threads = []

    for _ in range(5):
        thread = Thread(target=worker_deposit, args=(account,))
        threads.append(thread)

    for _ in range(5):
        thread = Thread(target=worker_withdrawal, args=(account,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(Fore.MAGENTA + f'Saldo: {account.get_saldo()}')