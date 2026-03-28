'''
Komunikacja dwukierunkowa (Pipe)
Użyj multiprocessing.Pipe do stworzenia dwukierunkowej komunikacji. Proces nadrzędny
wysyła do procesu potomnego listę liczb. Proces potomny oblicza ich sumę i średnią, a
następnie odsyła krotkę z wynikami ((suma, srednia)) do procesu nadrzędnego, który je
drukuje.
'''

from multiprocessing import Pipe, Process
import time

def worker(conn):
    numbers = conn.recv()

    total = sum(numbers)
    average = total / len(numbers)

    conn.send((total, average))
    conn.close()


if __name__ == "__main__":
    parent_numbers = [1, 2, 3, 4, 5]

    #create pipe
    parent_conn, child_conn = Pipe()
    #create process for worker
    p = Process(target=worker, args=(child_conn,))

    # Start process
    p.start()
    # Send data through pipe
    parent_conn.send(parent_numbers)
    # Receive data through pipe
    result = parent_conn.recv()

    # Wait for the process to finish and then join
    p.join()

    print(result)