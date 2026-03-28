"""
Równoległe liczenie słów w plikach
Napisz program, który liczy łączną liczbę wystąpień danego słowa we wszystkich plikach.txt w bieżącym katalogu.
Każdy plik powinien być przeszukiwany w osobnym wątku. Wyniki zliczania z każdego wątku powinny być bezpiecznie
dodane do wspólnego licznika.
"""

from threading import Lock, Thread
import os

total_counter = 0
lock = Lock()


def open_text_file(file_name):
    encodings = [
        "utf-8",
        "utf-8-sig",
        "utf-16",
        "utf-16-le",
        "utf-16-be",
        "cp1250",
    ]
    # try for different encodings
    for encoding in encodings:
        try:
            with open(file_name, "r", encoding=encoding, errors="strict") as f:
                f.read(1024) # read first 1024 bytes (Workaround for encoding "errors with courtesy of Windows")
            return open(file_name, "r", encoding=encoding, errors="strict")
        except UnicodeDecodeError:
            pass
    return open(file_name, "r", encoding="latin-1", errors="replace")

def count_word(word, file_name):
    global total_counter
    counter = 0
    word_lower = word.lower().strip()

    if not word_lower:
        return

    with open_text_file(file_name) as f:
        for line in f:
            line_lower = line.lower()
            counter += line_lower.count(word_lower)

    with lock:
        total_counter += counter


if __name__ == "__main__":
    search = input("Podaj szukane słowo: ")

    txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]

    threads = []

    for file in txt_files:
        thread = Thread(target=count_word, args=(search, file))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Sprawdzone pliki: {len(txt_files)}\n{txt_files}\n")
    print(f"Wszystkich wystąpień szukanego słowa '{search}': {total_counter}")
