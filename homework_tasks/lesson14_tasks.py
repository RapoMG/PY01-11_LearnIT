"""Homework for lesson 12"""

from functools import wraps
import sqlite3  # tasks 1-10


def task_separator(last=False):
    """
    Separates successive functions called after each other with header and input() based pause at the end of its execution.

    :param last: if True omits pause at the end. *Default:* False 
    """

    def wrapper(func):

        @wraps(func)
        def call(*args, **kwargs):
            line_l = '<<< '
            line_r = ' >>>'
            title = func.__name__
            instr = func.__doc__

            title = title.replace("task", "task ")
            
            print(f"\n{line_l * 2} {title.upper()} {line_r * 2}\n")
            print(f"Instructions: \n \t{instr}\n\nCode execution:\n")

            result = func(*args, **kwargs)

            if not last: input("\nPress [Enter] for the next function\n") 

            return result
        
        return call

    return wrapper


########## TASKS #########

@task_separator()
def task1():
    """Stwórz tabelę książek
Napisz skrypt, który połączy się z bazą biblioteka.db i stworzy w niej tabelę ksiazki. Tabela
powinna mieć następujące kolumny:
id (INTEGER, klucz główny)
tytul (TEXT, nie może być pusty)
autor (TEXT, nie może być pusty)
rok_wydania (INTEGER)
    """
    #import sqlite3

    conn = sqlite3.connect("biblioteka.db")
    c = conn.cursor()

    print("Connected with db")

    c.execute("""
              CREATE TABLE IF NOT EXISTS ksiazki (
              id INTEGER PRIMARY KEY,
              tytul TEXT NOT NULL,
              autor TEXT NOT NULL,
              rok_wydania INTEGER)
              """)

    conn.commit()

    conn.close()

@task_separator()
def task2():
    """Dodaj książki
Napisz skrypt, który doda do tabeli ksiazki (stworzonej w zadaniu 1) trzy dowolne książki.
Użyj metody executemany do dodania wszystkich książek za jednym razem.
    """
    conn = sqlite3.connect("biblioteka.db")

    c = conn.cursor()

    book_list = [
        ("Spytaj milicjanta", "Krzysztof Grabowski", 2025),
        ("Kroniki Czarnej Kompanii", "Glen Cook", 2009),
        ("Nocny patrol", "Sergiej Łukjanienko", 2077)
        ]

    c.executemany("INSERT INTO ksiazki (tytul, autor, rok_wydania) VALUES (?, ?, ?)", book_list)

    conn.commit()

    print(f"{c.rowcount} records apended to 'ksiazki' table.")

    conn.close()

@task_separator()
def task3():
    """Wyświetl całą bibliotekę
Napisz skrypt, który pobierze i wyświetli w konsoli wszystkie książki (wszystkie kolumny) z
tabeli ksiazki.
    """
    conn = sqlite3.connect("biblioteka.db")
    c = conn.cursor()
    
    c.execute("SELECT * FROM ksiazki")

    books = c.fetchall()

    print("Current records from ksiazki table:")
    for book in books:
        print(f"Title: '{book[1]}' by {book[2]}, print in {book[3]}.")

    conn.close()


@task_separator()
def task4():
    """Wyszukaj książki autora
Napisz skrypt, który pobierze i wyświetli tylko te książki z tabeli ksiazki, które zostały
napisane przez Twojego ulubionego autora.
    """

    conn = sqlite3.connect("biblioteka.db")
    c = conn.cursor()

    c.execute("SELECT * FROM ksiazki WHERE autor LIKE ?",("%Cook%",))

    search = c.fetchone()
    print("Searched book:")
    print(f"Title: '{search[1]}' by {search[2]}, print in {search[3]}.")

    conn.close()


@task_separator()
def task5():
    """Zaktualizuj rok wydania
Wybierz jedną z dodanych książek i napisz skrypt, który zaktualizuje jej rok_wydania na
inną wartość. Po aktualizacji wyświetl dane tej książki, aby potwierdzić, że zmiana się
powiodła.
    """

    conn = sqlite3.connect("biblioteka.db")
    c = conn.cursor()

    c.execute("UPDATE ksiazki SET rok_wydania = ? WHERE tytul LIKE ?", (2007, "Nocny%"))

    conn.commit()

    c.execute("SELECT * FROM ksiazki WHERE tytul LIKE ?", ("Nocny%",))

    updated = c.fetchone()

    print(f"Record updated:\n Title: '{updated[1]}' by {updated[2]}, print in {updated[3]}.")

    conn.close()
    

@task_separator()
def task6():
    """Dwie tabele: Studenci i Audytoria
Napisz skrypt, który w nowej bazie uczelnia.db stworzy dwie tabele:studenci z kolumnami:
id_studenta (klucz główny), imie (TEXT), nazwisko(TEXT).
audytoria z kolumnami: id_audytorium (klucz główny), nazwa_budynku (TEXT),
numer_sali (INTEGER).
    """
    conn = sqlite3.connect("uczelnia.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS studenci(
              id_studenta INTEGER PRIMARY KEY,
              imie VARCHAR(20) NOT NULL,
              nazwisko VARCHAR(20) NOT NULL)
    """)

    c.execute("""CREATE TABLE IF NOT EXISTS audytoria(
              id_audytorium INTEGER PRIMARY KEY,
              nazwa_budynku TEXT NOT NULL,
              numer_sali INTEGER)
    """)
    conn.commit()

    print("Tables created.")
    conn.close()


@task_separator()
def task7():
    """Wypełnij dane uczelni
Napisz skrypt, który wypełni tabele studenci i audytoria przykładowymi danymi. Dodaj co
najmniej 4 studentów i 3 audytoria.
    """

    conn = sqlite3.connect("uczelnia.db")
    c = conn.cursor()

    students = [
        ("Andrzej", "Pilipiuk"),
        ("Rafał", "Kosik"),
        ("Maja","Kossakowska"),
        ("Paulina","Braiter"),
        ]
    
    auditoriums= [
        ("Główny", 8),
        ("Neofilologucum", 5),
        ("Neofilologucum", 7),
        ("Główny", 29),
        ]
    
    c.executemany("INSERT INTO studenci (imie, nazwisko) VALUES (?, ?)", students)
    c.executemany("INSERT INTO audytoria (nazwa_budynku, numer_sali) VALUES (?, ?)", auditoriums)

    conn.commit()

    print("Data stored into tables")

    conn.close()


@task_separator()
def task8():
    """Połącz tabele (Relacja)
To zadanie wprowadza kluczowe pojęcie relacji. Chcemy przypisać studentów do
audytoriów (np. na egzamin). Aby to zrobić, stwórz trzecią tabelę o nazwie przypisania w tej
samej bazie uczelnia.db. Tabela powinna mieć strukturę:
id_przypisania (INTEGER, klucz główny)
id_studenta (INTEGER) – będzie to tzw. klucz obcy wskazujący na id_studenta w
tabeli studenci .
id_audytorium (INTEGER) – klucz obcy wskazujący na id_audytorium w tabeli
audytoria.
    """

    conn = sqlite3.connect("uczelnia.db")

    c = conn.cursor()

    #conn.execute("PRAGMA foreign_keys = ON")

    c.execute("""
              CREATE TABLE egzamin(
              id_przypisania INTEGER PRIMARY KEY,
              id_studenta INTEGER NOT NULL,
              id_audytorium INTEGER NOT NULL,
              FOREIGN KEY(id_studenta) REFERENCES studenci(id_studenta),
              FOREIGN KEY(id_audytorium) REFERENCES audytoria(id_audytorium))
              """)
    
    conn.commit()

    print("'egzamin' relationship table created")

    conn.close()
    

@task_separator()
def task9():
    """Dokonaj przypisań
Napisz skrypt, który dokona przypisań. Dla każdego studenta z tabeli studenci dodaj wpis
do tabeli przypisania, łącząc go z jednym z audytoriów.
    """
    conn = sqlite3.connect("uczelnia.db")

    c = conn.cursor()

    exams = [
        (1, 1),
        (2, 3),
        (3, 4),
        (4, 3),
        (2, 4),
        (1, 2)]
              
    c.executemany("INSERT INTO egzamin (id_studenta, id_audytorium) VALUES (?, ?)", exams)

    conn.commit()
    
    print("Exam auditoriums assigned.")

    conn.close()
    
    
@task_separator(True)
def task10():
    """Funkcja wyszukująca z JOIN
Napisz funkcję w Pythonie znajdz_sale_studenta(nazwisko), która przyjmuje nazwisko
studenta jako argument. Funkcja powinna połączyć się z bazą, a następnie znaleźć i
wyświetlić informację, w którym budynku i w jakiej sali znajduje się dany student.
    """
    #import sqlite3

    def znajdz_sale_studenta(nazwisko: str):
        conn = sqlite3.connect("uczelnia.db")
        c = conn.cursor()
        
        c.execute("""
                  SELECT s.nazwisko, s.imie, a.nazwa_budynku, a.numer_sali
                  FROM egzamin e 
                  INNER JOIN studenci s ON e.id_studenta = s.id_studenta
                  INNER JOIN audytoria a ON e.id_audytorium = a.id_audytorium
                  WHERE s.nazwisko = ?
                  """, (nazwisko,)
                  )

        exams = c.fetchall()

        for exam in exams:
            print(f"{exam[0]} {exam[1]}: Budynek {exam[2]}, sala {exam[3]}.")
        
        conn.close()

    znajdz_sale_studenta("Kosik")


if __name__ == "__main__":
    task1()
    task2()
    task3()
    task4()
    task5()
    task6()
    task7()
    task8()
    task9()
    task10()
 