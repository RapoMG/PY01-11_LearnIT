'''
Równoległe haszowanie plików
Napisz skrypt, który oblicza skrót SHA256 dla każdego pliku w danym katalogu. Użyj
multiprocessing.Pool, aby rozdzielić listę plików między dostępne rdzenie procesora. Program
powinien na końcu wydrukować słownik, gdzie kluczem jest nazwa pliku, a wartością jego hash.
'''

import hashlib
import os
#import multiprocessing 
from multiprocessing import Pool

def hash_file(file_path):
    with open(file_path, 'rb') as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash

if __name__ == "__main__":
    
    # files in this dir
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    with Pool() as pool:
        hashes = {f: pool.apply_async(hash_file, args=(f,)).get() for f in files}

    pool.join()
    
    #print(hashes)

    # print dict in user-friendly format
    print('{')
    
    for file, hash in hashes.items():
        print(f"{file}: {hash},")
    
    print('}')
   