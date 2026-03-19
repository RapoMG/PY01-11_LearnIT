from unittest import result


def task_separator(func):
    def wrapper():
        line_l = '<<< '
        line_r = ' >>>'
        title = func.__name__

        try:
            title = title.replace("greet", "task ")
        except:
            pass

        print(f"\n{line_l * 2} {title.upper()} {line_r * 2}\n")
        func()
    return wrapper

@task_separator
def task1():
    '''Kalkulator: Napisz funkcję kalkulator(a, b, operacja) , która przyjmuje dwie liczby i
string z operacją ( "+" , "-" , "*" lub / "). Funkcja powinna zwracać wynik
odpowiedniego działania.'''

    def calculator(a, b, operation):
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return a / b
        else:
            return "Nieznana operacja"
    
    def get_number():
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            operation = input("Enter the operation (+, -, *, /): ")
            return calculator(a, b, operation)
        
        except ValueError:
            print("Invalid number. Please try again.\n")
        except ZeroDivisionError:
            print("Cannot divide by zero. Please try again.\n")

        
            
    while True:
        result = get_number()
        print(f"Result: {result}\n")
        _next = input("Do you want to perform another calculation? (yes/no): ")
        if _next.lower() == "no":
            break
        

@task_separator
def task2():
    '''Informacje o książce: Stwórz funkcję opis_ksiazki(tytul, autor,
rok_wydania=2024) . Funkcja powinna zwracać sformatowany string, np. "Książka
'[Tytuł]' została napisana przez [Autor] i wydana w roku [Rok wydania]." .
Przetestuj ją, wywołując z argumentami pozycyjnymi i nazwanymi.'''

    def book_info(title, author, publication_year=2024):
        return f"Książka '{title}' została napisana przez {author} i wydana w roku {publication_year}."

    # positional arguments
    print(book_info("Wiedźmin", "Andrzej Sapkowski", 1993))

    # named arguments
    print(book_info(author="Frank Herbert", title="Diuna", publication_year=1965))

@task_separator
def task3():
    '''Średnia ocen: Napisz funkcję oblicz_srednia(*args), która przyjmuje dowolną liczbę
ocen (argumentów pozycyjnych) i zwraca ich średnią arytmetyczną. Jeśli nie podano żadnej
oceny, powinna zwrócić 0.'''

    def calculate_average(*args):
        if len(args) == 0:
            return 0
        return sum(args) / len(args)

    print(calculate_average(4, 5, 3, 4))
    print(calculate_average())


@task_separator
def task4():
    '''Sprawdzanie zakresu: Zdefiniuj zmienną globalną POZIOM_DOSTEPU = "user" . Napisz
funkcję, która próbuje zmienić tę zmienną na "admin" bez użycia słowa kluczowego
global . Wewnątrz funkcji stwórz zmienną lokalną o tej samej nazwie. Wyświetl wartość
zmiennej wewnątrz i na zewnątrz funkcji, aby zobaczyć różnicę.'''

    global POZIOM_DOSTEPU
    POZIOM_DOSTEPU = "user"

    def change_access_level():
        POZIOM_DOSTEPU = "admin"  # This creates a local variable, not changing the global one
        print(f"Inside function: {POZIOM_DOSTEPU}")

    print(f"Before function call: {POZIOM_DOSTEPU}")
    change_access_level()
    print(f"After function call: {POZIOM_DOSTEPU}")


@task_separator
def task5():
    '''Adnotacje i docstring: Weź funkcję kalkulator z zadania 1. Dodaj do niej pełne
adnotacje typów dla wszystkich parametrów i wartości zwracanej. Napisz również
kompletny docstring opisujący jej działanie.'''

    def calculator(a: float, b: float, operation: str) -> float | str:
        """
        Performs a basic arithmetic operation on two numbers.

        Parameters:
        a (float): The first number.
        b (float): The second number.
        operation (str): A string representing the operation to perform. 
                         It can be one of the following: "+", "-", "*", "/".

        Returns:
        float: The result of the arithmetic operation. If an unknown operation is provided, returns a string message.
        """
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return a / b
        else:
            return "Nieznana operacja"


@task_separator
def task6():
    '''Wielokrotne powitanie: Napisz funkcję wielokrotne_powitanie(imie: str, ilosc:
int) -> None , która wyświetla powitanie f"Cześć, {imie}!" tyle razy, ile wynosi
ilosc . Ta funkcja nie powinna niczego zwracać.'''

    def multiple_greetings(name: str, count: int) -> None:
        for _ in range(count):
            print(f"Cześć, {name}!")

    multiple_greetings("Alice", 3)


@task_separator
def task7():
    '''Zwracanie wielu wartości: Stwórz funkcję analiza_listy(lista: list[int]) , która
przyjmuje listę liczb i zwraca krotkę zawierającą trzy wartości: minimum, maksimum i sumę
elementów z listy.'''

    def analyze_list(lst: list[int]) -> tuple[int, int, int] | str:
        if not lst or len(lst) == 0:
            return "No elements in the list"  # Return a message for an empty list
        minimum = min(lst)
        maximum = max(lst)
        total_sum = sum(lst)
        return (minimum, maximum, total_sum)

    result = analyze_list([3, 1, 4, 1, 5])
    print(f"Minimum: {result[0]}, Maximum: {result[1]}, Sum: {result[2]}")


@task_separator
def task8():
    '''Tworzenie profilu: Napisz funkcję stworz_profil(imie, **dane_dodatkowe) , która
przyjmuje imię oraz dowolną liczbę nazwanych argumentów (np. wiek=30 ,
miasto="Warszawa" ). Funkcja powinna zwrócić słownik z profilem użytkownika, gdzie
klucz 'imie' jest obowiązkowy, a reszta danych jest pobierana z **dane_dodatkowe .'''

    def create_profile(name: str, **additional_data) -> dict:
        profile = {"imie": name}
        profile.update(additional_data)
        return profile

    user_profile = create_profile("Bob", wiek=30, miasto="Warszawa")
    print(user_profile)


@task_separator
def task9():
    '''Silnia (rekurencja): Napisz funkcję silnia(n: int) -> int , która oblicza silnię liczby n
w sposób rekurencyjny (czyli wywołując samą siebie). Pamiętaj o warunku bazowym: silnia
z 0 to 1. (Wzór: n! = n * (n-1)! ).'''

    def factorial(n: int) -> int:
        if n < 0:
            raise ValueError("Silnia nie jest zdefiniowana dla liczb ujemnych.")
        elif n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    print(factorial(5))  # Output: 120
    print(factorial(0))  # Output: 1
    

@task_separator
def task10():
    '''Walidator hasła: Stwórz funkcję sprawdz_haslo(haslo: str) -> bool .
Funkcja powinna sprawdzać, czy hasło spełnia następujące warunki i zwracać True lub False :
    * Ma co najmniej 8 znaków.
    * Zawiera co najmniej jedną wielką literę.
    * Zawiera co najmniej jedną cyfrę.
    Napisz do niej pełną dokumentację (docstring i adnotacje).'''

    def check_password(password: str) -> bool:
        """
        Validates a password based on specific criteria.
        * The password must be at least 8 characters long.
        * It must contain at least one uppercase letter.
        * It must contain at least one digit.

        Parameters:
        password (str): The password string to validate.

        Returns:
        bool: True if the password is valid, False otherwise.
        """
        if len(password) < 8:
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.isdigit() for char in password):
            return False
        return True
    
    print(check_password("Password123"))  # Output: True
    print(check_password("password"))      # Output: False (no uppercase letter and no digit)
    print(check_password("PASSWORD"))      # Output: False  (no digit)
    print(check_password("Pass123"))      # Output: False (less than 8 characters)


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
