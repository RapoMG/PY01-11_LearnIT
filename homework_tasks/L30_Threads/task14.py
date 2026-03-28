# -*- coding: utf-8 -*-
"""
Kopiowanie plików w tle
Napisz program, który kopiuje wszystkie pliki z jednego katalogu do drugiego. Każdy plik
powinien być kopiowany w osobnym wątku. Wyświetlaj postęp, np. "Kopiowanie pliku X...",
"Ukończono kopiowanie pliku X". Program główny powinien zakończyć się dopiero po
skopiowaniu wszystkich plików.
"""

from pathlib import Path
import threading
from colorama import Fore, init


def copy_file(src: Path, dst: Path):
    print(Fore.YELLOW + f"Kopiowanie pliku {src.name}...")
    with src.open("rb") as f_in, dst.open("wb") as f_out:
        f_out.write(f_in.read())
    print(Fore.GREEN + f"Ukończono kopiowanie pliku {src.name}.")


def copy_files(src_dir: Path, dst_dir: Path):
    if not dst_dir.is_dir():
        print(Fore.GREEN + f"KATALOG UTWORZONY.")
        dst_dir.mkdir(parents=True, exist_ok=True)

    threads = []
    for src in src_dir.iterdir():
        if not src.is_file():
            continue
        dst = dst_dir / src.name
        thread = threading.Thread(target=copy_file, args=(src, dst))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    init()

    src_dir = Path(r"K:\Przestrzeń robocza\Python\VS_Code")
    dst_dir = Path(r"K:\Przestrzeń robocza\Python\VS_Code\copy_for_L30")

    print()
    if not src_dir.is_dir():
        print(Fore.RED + f"ŹRÓDŁOWY KATALOG NIE ISTNIEJE.\n{src_dir}")
    if not dst_dir.is_dir():
        print(Fore.RED + f"DOCELOWY KATALOG NIE ISTNIEJE. \n{dst_dir}")
    
    if src_dir.is_dir():
        copy_files(src_dir, dst_dir)
