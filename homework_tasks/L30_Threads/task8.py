'''
Komunikacja z procesem
Stwórz proces, który prosi użytkownika o podanie imienia (input()), a następnie wysyła to
imię do procesu nadrzędnego za pomocą multiprocessing.Queue. Proces nadrzędny
odbiera imię i drukuje "Witaj, [imię]!".
'''

from multiprocessing import Process, Queue


def ask_name(queue):
    try:
        name = input("Podaj imie: \n")
    except EOFError as e:
        # Some environments don't allow stdin in child processes.
        print(f'An error occurred: {e}\nBypassing stdin in child process.\n')
        name = None
    queue.put(name)

if __name__ == '__main__':
    queue = Queue()
    process = Process(target=ask_name, args=(queue,))

    process.start()
    name = queue.get()
    
    if name is None:
        name = input("Podaj imie: \n")
    process.join()

    print(f"Witaj, {name}!")
