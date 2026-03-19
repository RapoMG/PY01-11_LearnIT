"""Homework for lesson 12"""

from functools import wraps
from dataclasses import dataclass, field  # task 1, 2, 6, 7, 9
from inspect import isfunction  # task 10


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
    """Klasa danych Film
Stwórz klasę danych (@dataclass) o nazwie Film, która będzie przechowywać tytuł (string),
reżysera (string) i rok_produkcji (integer). Utwórz dwie instancje tej klasy i wyświetl je."""

    #from dataclasses import dataclass

    @dataclass
    class Film:
        title: str
        director: str
        prod_year: int

    
    f1 = Film("Star Wars", "George Lucas", 1977)
    f2 = Film("The Fifth Element", "Luc Besone", 1997)

    print(f1.__str__())
    print(f2.__str__())


@task_separator()
def task2():
    """Walidator wieku
Stwórz klasę Uzytkownik z atrybutem _wiek. Użyj dekoratora @property, aby stworzyć
właściwość wiek. Getter powinien zwracać wiek, a setter powinien sprawdzać, czy podany
wiek jest w zakresie od 0 do 120. Jeśli nie jest, powinien wyświetlić komunikat błędu i nie
zmieniać wartości."""

    @dataclass
    class User:
        _age: int

        @property
        def age(self):
            return self._age
        
        @age.setter
        def age(self, new_age):
            if new_age in range(0,120):
                self._age = new_age
            else:
                print("Age out of the range!")
            

    u = User(50)
    print(u.age)
    
    # new age right
    u.age = 60 
    print(u.age)

    # new age wrong
    u.age = 125
    print(u.age)

@task_separator()
def task3():
    """Konwerter Walut
Stwórz klasę KalkulatorWalut. Dodaj w niej metodę statyczną (@staticmethod) o nazwie
usd_na_pln, która przyjmuje kwotę w dolarach i zwraca ją przeliczoną na złotówki (przyjmij
stały kurs, np. 1 USD = 4.0 PLN). Wywołaj tę metodę bez tworzenia obiektu klasy."""


    class CurrencyCalc:

        @staticmethod
        def usd_to_pln(usd):
            exchange = 4.0
            return usd * exchange
        
    
    print(CurrencyCalc.usd_to_pln(75.99))
   

@task_separator()
def task4():
    """Bezpieczne dzielenie
Napisz funkcję bezpieczne_dzielenie(a, b), która zwraca wynik dzielenia a / b. Użyj bloku
try...except, aby obsłużyć błąd ZeroDivisionError. Jeśli wystąpi ten błąd, funkcja powinna
zwrócić None i wyświetlić komunikat "Błąd: Dzielenie przez zero!"."""

   
    def secure_division(a, b) -> float|None:
        try:
            return a/b
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            return None
        
    print(f"{secure_division(3,7):.02f}")
    print(secure_division(12,0))


@task_separator()
def task5():
    """Odczyt pliku
Napisz program, który próbuje otworzyć i odczytać plik o nazwie nieistniejacy.txt. Użyj bloku
try...except, aby obsłużyć wyjątek FileNotFoundError i wyświetlić przyjazny komunikat
użytkownikowi."""

    def wrong_file_example():
        name = "nofile.txt"

        try:
            with open(name, "r", encoding="utf-8") as f:
                return f.read()
        except FileExistsError as e:
            return e
        
    try:
        wrong_file_example()
    except FileNotFoundError as e:
        print(f"Error: {e.args[1]}")
    

@task_separator()
def task6():
    """Własny wyjątek InvalidPasswordError
Stwórz własny wyjątek InvalidPasswordError. Następnie napisz funkcję ustaw_haslo(haslo),
która sprawdza, czy hasło ma co najmniej 8 znaków. Jeśli nie, funkcja powinna podnieść
(raise) wyjątek InvalidPasswordError z odpowiednim komunikatem. Napisz kod, który
testuje tę funkcję w bloku try...except."""

    class InvalidPasswordError(Exception):
        pass
    
    @dataclass
    class Password:
        _password: str = field(init=False, default="")
        
        def set_password(self, password):
            if len(password) < 8:
                raise InvalidPasswordError("Password to short.")
            else:
                self._password = password

    
    try:
        p = Password().set_password("1234567")
    except InvalidPasswordError as e:
        print(e)
       
   
@task_separator()
def task7():
    """Alternatywny konstruktor dla Daty
Stwórz klasę Data z atrybutami dzien, miesiac, rok. Dodaj metodę klasy (@classmethod) o
nazwie ze_stringa, która przyjmuje datę w formacie "DD-MM-RRRR" (np. "25-12-2023") i
tworzy na jej podstawie obiekt klasy Data. Pamiętaj o konwersji typów na int. """

    @dataclass
    class Date:
        day: int
        month: int
        year: int

        @classmethod
        def form_string(cls, date: str):
            "accept's adte format DD-MM-YYYY"
            date_parts = date.split("-")
            return Date(int(date_parts[0]), int(date_parts[1]), int(date_parts[2]))
        
        def date_str(self):
            return f"{self.day:02d}.{self.month:02d}.{self.year}"
        
    
    d = Date.form_string("12-05-2000")

    print(d.date_str())


@task_separator()
def task8():
    """Kalkulator z pełną obsługą błędów
Stwórz prosty kalkulator, który prosi użytkownika o podanie dwóch liczb i operacji (+, -, *, /).
Całość umieść w pętli while True , aby program działał do momentu przerwania.
Użyj bloku try...except do obsługi:
ValueError , jeśli użytkownik wpisze coś, co nie jest liczbą.
ZeroDivisionError przy próbie dzielenia przez zero.
Użyj bloku else , aby wyświetlić wynik tylko wtedy, gdy nie było błędu.
Użyj bloku finally , aby na koniec każdej iteracji pętli wyświetlić komunikat "Koniec obliczeń."."""
    
    class Calc:

        @staticmethod
        def add(a: float, b: float) -> float:  
            return a + b

        @staticmethod
        def subtraction(a: float, b: float) -> float:
            return a - b
            
        @staticmethod
        def division(a: float, b: float) -> float:
            if b == 0:
                raise ZeroDivisionError("Division by 0")
            return a / b
    
        
        @staticmethod
        def multiplication(a: float, b: float) -> float|Exception:
            return a * b
            

    def app():            
        while True:
            try:
                oper = input("\nEnter operator [ * / + - ] for operation to calculate or [ q ] to quit\n")
                if oper.strip().lower() == "q":
                    print("\nClosing app.")
                    break
                a = float(input("\nEnter the first value:\n"))
                b = float(input("\nEnter the second value:\n"))
            except ValueError:
                print(f"Error: That is not a proper number.")
            else:
                try:
                    if oper.strip() == "*":
                        result = Calc.multiplication(a, b)
                    elif oper.strip() == "/":
                        result = Calc.division(a, b)
                    elif oper.strip() == "+":
                        result = Calc.add(a, b)
                    elif oper.strip() == "-":
                        result = Calc.subtraction(a, b)
                except ZeroDivisionError as e:
                    print(f"Error: {e}")
                else:
                    print(f"\n{a} {oper} {b} = {result}\n")
            finally:
                print("End of calculation.\n")

    app()
    

@task_separator()
def task9():
    """Klasa KontoBankowe z property i wyjątkami
Stwórz klasę KontoBankowe za pomocą @dataclass, która ma atrybut _saldo (prywatne).
Stwórz właściwość ( @property ) saldo , która tylko odczytuje wartość _saldo .
Stwórz metodę wplac(kwota) , która dodaje kwotę do salda. Metoda powinna podnosić
ValueError , jeśli kwota jest ujemna.
Stwórz metodę wyplac(kwota) , która odejmuje kwotę od salda. Metoda powinna
podnosić ValueError , jeśli kwota do wypłaty jest ujemna, oraz własny wyjątekBrakSrodkowError , jeśli saldo jest niewystarczające.
Przetestuj działanie klasy, obsługując wszystkie możliwe wyjątki."""

    class InsufficientFundsError(Exception):
        pass

    @dataclass
    class BankAccount:
        _balance: float = field(init=False, default=0.0)

        @property
        def balance(self) -> float:
            return self._balance
        
        def deposit(self, value: float):
            if value < 0:
                raise ValueError("Deposit cannot be negative.")
            self._balance += value

        def withdrawal(self, value: float):
            if value < 0:
                raise ValueError("Withdrawl cannot be negative.")
            if value > self.balance:
                raise InsufficientFundsError("Insufficient funds in account.")
            self._balance -= value


    acc = BankAccount()
    
    actions = [
        lambda: print(acc.balance),
        lambda: acc.withdrawal(5.0),
        lambda: acc.withdrawal(-5),
        lambda: acc.deposit(-5),
        lambda: acc.deposit(5),
        lambda: print(acc.balance),
        lambda: acc.withdrawal(5),
        lambda: print(acc.balance),
        ]

    oper = 0
    while len(actions) > oper:
        try:
            actions[oper]()
        except (ValueError, InsufficientFundsError) as e:
            print(f"Error {e}")
        finally:
            oper += 1
    
    
@task_separator(True)
def task10():
    """Metaklasa walidująca
Stwórz metaklasę MetaWalidujMetody, która podczas tworzenia nowej klasy sprawdza, czy
wszystkie jej metody (poza metodami "magicznymi", czyli zaczynającymi się od __) mają
docstring. Jeśli któraś metoda go nie ma, metaklasa powinna podnieść TypeError z
informacją, która metoda wymaga dokumentacji. Przetestuj ją, tworząc klasę z poprawnie i
niepoprawnie udokumentowanymi metodami."""

    # from inspect import isfunction

    class MetaWalidujMetody(type):
        def __new__(mcls, cls_name, super_classes, attribute_dict):
            # cls_name - name of created clas
            # super_classes -  classes to inherit from (in the form of tuple)
            # attribute_dict - attributes of class (in the form of dictionary)

            # go thru all class attributes
            for attr_name, value in attribute_dict.items():
                # Test if name starts with '__' anf if it's method (is function)
                if not attr_name.startswith("__") and isfunction(value): 
                    # Test if it has doc string
                    if value.__doc__ is None:
                        raise TypeError(f"Method '{attr_name}' in class '{cls_name}' has no docstring.")

            return super().__new__(mcls, cls_name, super_classes, attribute_dict)


    try:
        
        class MetTest(metaclass=MetaWalidujMetody):
            text = "that's text"
            some_list = [1,2]

            # with docstring
            def thatismethod(self):
                """That's docstring"""
                print(f"{self.text} inside method.")

            # without docstring
            def thatismethod2(self):
                print(f"{self.text} inside diferent method.")

    except TypeError as e:
        print(e)
    


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
 