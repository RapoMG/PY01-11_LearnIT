"""Homework for lesson 12"""

from dataclasses import dataclass  # taksk 10
from functools import wraps
import sqlite3


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

##### BASE CODE ########
def przygotuj_baze():
    """Tworzy i wypełnia bazę danych na potrzeby zadań."""
    conn = sqlite3.connect('sklep.db') # Tworzy plik sklep.db
    cursor = conn.cursor()

    # Usunięcie tabel, jeśli istnieją, dla czystego startu
    cursor.execute("DROP TABLE IF EXISTS Zamowienia_Produkty")
    cursor.execute("DROP TABLE IF EXISTS Zamowienia")
    cursor.execute("DROP TABLE IF EXISTS Produkty")
    cursor.execute("DROP TABLE IF EXISTS Kategorie")
    cursor.execute("DROP TABLE IF EXISTS Klienci")
    
    # Tworzenie tabel
    cursor.execute('''
    CREATE TABLE Kategorie (
        id_kategorii INTEGER PRIMARY KEY,
        nazwa_kategorii TEXT UNIQUE NOT NULL
        )''')
    
    cursor.execute('''
    CREATE TABLE Produkty (
        id_produktu INTEGER PRIMARY KEY,
        nazwa_produktu TEXT NOT NULL,
        cena REAL NOT NULL,
        id_kategorii INTEGER,
        FOREIGN KEY (id_kategorii) REFERENCES Kategorie(id_kategorii)
        )''')
    
    cursor.execute('''
    CREATE TABLE Klienci (
        id_klienta INTEGER PRIMARY KEY,
        imie TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
        )''')
    
    cursor.execute('''
    CREATE TABLE Zamowienia (
    id_zamowienia INTEGER PRIMARY KEY,
    id_klienta INTEGER,
    data_zamowienia DATE,
    FOREIGN KEY (id_klienta) REFERENCES Klienci(id_klienta)
    )''')

    cursor.execute('''
        CREATE TABLE Zamowienia_Produkty (
        id_zamowienia INTEGER,
        id_produktu INTEGER,
        ilosc INTEGER NOT NULL,
        PRIMARY KEY (id_zamowienia, id_produktu),
        FOREIGN KEY (id_zamowienia) REFERENCES Zamowienia(id_zamowienia),
        FOREIGN KEY (id_produktu) REFERENCES Produkty(id_produktu)
        )''')

    # Wstawianie danych
    kategorie = [('Elektronika',), ('Książki',), ('Dom i ogród',)]
    klienci = [('Anna Nowak', 'anna.n@example.com'), ('Jan Kowalski',
    'jan.k@example.com'), ('Zofia Wiśniewska', 'zofia.w@example.com')]

    produkty = [
    ('Laptop Pro', 5200.00, 1), ('Smartfon X', 2500.00, 1),
    ('Python dla każdego', 89.99, 2), ('Wzorce projektowe', 120.50, 2),
    ('Kosiarka elektryczna', 750.00, 3), ('Zestaw narzędzi', 300.00, 3),
    ('Słuchawki bezprzewodowe', 450.00, 1)
    ]

    zamowienia = [(1, '2023-10-01'), (2, '2023-10-02'), (1, '2023-10-05')]
    zamowienia_produkty = [(1, 1, 1), (1, 7, 1), (2, 3, 2), (3, 5, 1)]

    cursor.executemany("INSERT INTO Kategorie (nazwa_kategorii) VALUES (?)", kategorie)
    cursor.executemany("INSERT INTO Klienci (imie, email) VALUES (?,?)", klienci)

    cursor.executemany("INSERT INTO Produkty (nazwa_produktu, cena, id_kategorii) VALUES (?,?,?)", produkty)
    cursor.executemany("INSERT INTO Zamowienia (id_klienta, data_zamowienia) VALUES (?,?)", zamowienia)
    cursor.executemany("INSERT INTO Zamowienia_Produkty (id_zamowienia, id_produktu, ilosc) VALUES (?,?,?)", zamowienia_produkty)

    conn.commit()
    conn.close()

    print("\nBaza 'sklep.db' została przygotowana.")

########## TASKS #########

@task_separator()
def task1():
    """Liczba produktów
Napisz skrypt, który połączy się z bazą sklep.db i policzy, ile jest wszystkich produktów w
tabeli Produkty. Użyj funkcji COUNT().
    """
    conn = sqlite3.connect("sklep.db")
    c = conn.cursor()

    c.execute("SELECT COUNT(id_produktu) FROM Produkty")

    sum_ = c.fetchone()

    print(f"Dostęne produkty: {sum_[0]}")

    conn.close()


@task_separator()
def task2():
    """Najdroższy produkt
Napisz skrypt, który znajdzie nazwę i cenę najdroższego produktu w sklepie. Użyj funkcji
MAX().
    """
    conn = sqlite3.connect("sklep.db")
    c = conn.cursor()

    c.execute("""SELECT nazwa_produktu, cena FROM Produkty
              WHERE cena = (
              SELECT MAX(Cena) FROM Produkty
              )
              """)

    max_ = c.fetchone()

    print(max_)
    print(f"Najdroższy produkt: {max_[0]}, cena: {max_[1]:.2f}")

    conn.close()


@task_separator()
def task3():
    """Suma wartości
Oblicz i wyświetl łączną wartość wszystkich produktów z kategorii "Elektronika". Użyj funkcji
SUM() oraz klauzuli WHERE z JOIN.
    """

    conn = sqlite3.connect("sklep.db")
    c = conn.cursor()

    kat = "Elektronika"

    c.execute("""SELECT SUM(p.cena), k.nazwa_kategorii
              FROM Kategorie k
              INNER JOIN Produkty p ON k.id_kategorii = p.id_kategorii
              WHERE k.nazwa_kategorii = ? """, (kat,) 
              )
    
    sum_ = c.fetchone()

    print(f"Suma cen produktów z kategorii {kat}: {sum_[0]}\n")

    conn.close()


@task_separator()
def task4():
    """Średnia cena książki
Napisz zapytanie, które obliczy średnią cenę produktów w kategorii "Książki". Użyj AVG().
    """

    conn = sqlite3.connect("sklep.db")
    c = conn.cursor()

    kat = "Książki"

    c.execute("""
              SELECT AVG(p.cena)
              FROM Kategorie k
              INNER JOIN Produkty p ON p.id_kategorii = k.id_kategorii
              WHERE k.nazwa_kategorii = ? """, (kat,)
              )
    
    avg = c.fetchone()

    print(f"Średnia cena produktów z kategorii {kat}: {avg[0]:.2f}\n")

    conn.close()


@task_separator()
def task5():
    """Lista klientów
Napisz skrypt, który wyświetli imiona i adresy e-mail wszystkich klientów z tabeli Klienci.
    """
    conn = sqlite3.connect("sklep.db")
    c = conn.cursor()

    c.execute("SELECT imie, email FROM Klienci")

    customers = c.fetchall()

    print("Klienci:")
    for customer in customers:
        print(f"{customer[0]}: {customer[1]}")

    conn.close()


@task_separator()
def task6():
    """Produkty droższe od średniej
Napisz skrypt, który wyświetli nazwy i ceny wszystkich produktów, których cena jest wyższa
niż średnia cena wszystkich produktów w sklepie. Wykorzystaj podzapytanie.
    """
    conn = sqlite3.connect("Sklep.db")
    c = conn.cursor()

    c.execute("""
              SELECT nazwa_produktu, cena FROM Produkty
              WHERE cena > (SELECT AVG(cena) FROM Produkty)
              """)

    products = c.fetchall()

    print("Produkty o cenie powyżej średniej:")
    for p in products:
        print(f"{p[0]}, cena: {p[1]:.2f}")

    conn.close()

   
@task_separator()
def task7():
    """Zamówienia Anny Nowak
Napisz skrypt, który wyświetli nazwy wszystkich produktów zamówionych przez klienta o
imieniu 'Anna Nowak'. Będziesz potrzebować połączyć dane z czterech tabel: Klienci,
Zamowienia, Zamowienia_Produkty i Produkty.
    """
    conn = sqlite3.connect("sklep.db")
    c = conn.cursor()

    klient = "Anna Nowak"

    c.execute("""
              SELECT p.nazwa_produktu
              FROM Klienci k
              JOIN Zamowienia z ON z.id_klienta = k.id_klienta
              JOIN Zamowienia_Produkty zp ON zp.id_zamowienia = z.id_zamowienia
              JOIN Produkty p ON p.id_produktu = zp.id_produktu
              WHERE k.imie = ?
              """, (klient,))

    prod = c.fetchall()

    print(f"Produkty zamówione przez klienta {klient}:")
    for i, p in enumerate(prod):
        print(f"{i+1}. {p[0]}")

    conn.close()


@task_separator()
def task8():
    """Kategorie z liczbą produktów
Napisz zapytanie, które wyświetli nazwę każdej kategorii oraz liczbę produktów należących
do tej kategorii. Użyj JOIN, COUNT() oraz GROUP BY.
    """
    conn = sqlite3.connect("sklep.db")
    c = conn.cursor()

    c.execute("""
              SELECT k.nazwa_kategorii, (SELECT COUNT(p.id_produktu))
              FROM Kategorie k
              JOIN Produkty p ON p.id_kategorii = k.id_kategorii
              GROUP BY k.id_kategorii

              """)
    prods = c.fetchall()

    print("Liczba produktów w kategoriach:")
    for p in prods:
        print(f"\t{p[0]}:\t{p[1]}")

    conn.close()
    

@task_separator()
def task9():
    """Funkcja do wyszukiwania produktów
Napisz w Pythonie funkcję znajdz_produkty_w_kategorii(nazwa_kategorii), która przyjmuje
jako argument nazwę kategorii i zwraca listę krotek (nazwa_produktu, cena) dla wszystkich
produktów w tej kategorii.
    """
    def znajdz_produkty_w_kategorii(nazwa_kategorii: str)-> list[(str,float)]:
        conn = sqlite3.connect("sklep.db")
        c = conn.cursor()

        c.execute("""
                  SELECT p.nazwa_produktu, p.cena
                  FROM Produkty p
                  JOIN Kategorie k ON k.id_kategorii = p.id_kategorii
                  WHERE k.nazwa_kategorii = ?
                  ORDER BY p.nazwa_produktu
                  """,
                  (nazwa_kategorii.strip(),))
        
        prods = c.fetchall()

        conn.close()
    
        return prods
    
    znajdz_produkty_w_kategorii("Dom i Ogród")
    
    
@task_separator()
def task10():
    """Prosta symulacja ORM
Stwórz klasę Produkt w Pythonie z atrybutami id_produktu, nazwa_produktu i cena.
Następnie napisz funkcję pobierz_wszystkie_produkty(), która połączy się z bazą danych,
pobierze wszystkie produkty i zwróci listę obiektów klasy Produkt. To ćwiczenie pokaże Ci,
jak ORM automatyzuje mapowanie wierszy na obiekty.
    """
    @dataclass
    class Produkt:
        id_produktu: int
        nazwa_produktu: str
        cena: float


    def pobierz_wszystkie_produkty()-> list[object]:
        conn = sqlite3.connect("sklep.db")
        c = conn.cursor()

        c.execute("""
                  SELECT id_produktu, nazwa_produktu, cena FROM Produkty
                  """)
        prods = c.fetchall()
        conn.close()

        return [Produkt(p[0], p[1], p[2]) for p in prods]


    pobierz_wszystkie_produkty()


if __name__ == "__main__":
    przygotuj_baze()
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
 