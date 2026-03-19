

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
    """Tworzenie i typowanie: Utwórz zmienne przechowujące Twoje imię (str), wiek (int), średnią
ocen (float) i status studenta (bool). Wyświetl na ekranie wartość i typ każdej zmiennej."""
    name = "Adam"
    age = 12
    avrage_grade = 4.6
    student_status = True

    print(f"Variable name is {type(name)} and has value: {name}.")
    print(f"Variable age is {type(age)} and has value: {age}.")
    print(f"Variable avrage_grade is {type(avrage_grade)} and has value: {avrage_grade}.")
    print(f"Variable student_status is {type(student_status)} and has value: {student_status}.")

@task_separator
def task2():
    """Kalkulator BMI: Napisz program, który zapyta użytkownika o jego wagę w kilogramach i
wzrost w metrach. Oblicz i wyświetl wskaźnik masy ciała (BMI) według wzoru: BMI = waga
/ (wzrost * wzrost) ."""
    
    print("BMI calculator:")
    while True:
        try:
            mass = float(input("Enter the weight in kilograms\n"))
        except:
            continue
        try:
            height = float(input("Enter the height in meters\n"))
        except:
            continue
        bmi = mass / (height * height)
        print(f"\nCalculated BMI is {bmi:.2f}\n")
        end = input(f"\nPress [ENTER] for the next calculation or type [E] and press [ENTER] to exit.\n")
        print(end)
        if end.lower() == "e":
            break


@task_separator
def task3():
    """Analiza stringa: Utwórz zmienną z łańcuchem znaków " Python jest super! " .
Wykonaj następujące działania i wyświetl wynik każdego kroku:Usuń zbędne białe znaki na początku i na końcu.
Przekształć cały ciąg na małe litery.
Zamień słowo "super" na "świetny".
Wyświetl na ekranie znak pod indeksem 4 ."""

    text = " Python jest super! "
    print(text)

    text = text.strip()
    print(text)

    text = text.lower()
    print(text)

    text = text.replace("super", "świetny")
    print(text)

    print(text[4])


@task_separator
def task4():
    """Praca z f-stringami: Poproś użytkownika o jego imię i rok urodzenia. Oblicz jego
przybliżony wiek i wyświetl komunikat w formacie: "Cześć, [Imię]! W 2025 roku
będziesz mieć około [Wiek] lat."""

    while True:
        year = 2025
        try:
            name = input("What's your name?\n")
            born = int(input("What year you were born?\n"))
        except ValueError:
            continue
        if born > year:
            print(f"You weren't born yet in {year}.")
        else:
            break    

    print(f"Hi, {name}! In the {year}, you're be {year - born} years old." )



@task_separator
def task5():
    """Popraw kod zgodnie z PEP 8: Poniżej znajduje się fragment kodu. Przepisz go tak, aby
był zgodny z zasadami PEP 8.
# Kod źródłowy
NazwaUzytkownika="JanKowalski"
wiekUzytkownika=25
if wiekUzytkownika>=18:print(NazwaUzytkownika+' jest dorosły.')"""

    code = """
    nazwa_uzytkownika = 'JanKowalski'
    wiek_uzytkownika = 25
    if wiek_uzytkownika >= 18:
        print(nazwa_uzytkownika + ' jest dorosły.')"""
    
    print(code)


@task_separator
def task6():
    """Operacje na liście:
Utwórz listę owoce = ["jabłko", "banan", "wiśnia"] .
Dodaj na koniec listy "pomarańczę".
Zmień drugi element ("banan") na "jagodę".
Wyświetl końcową listę na ekran."""

    fruits = ["jabłko", "banan", "wiśnia"]
    print(fruits)

    fruits.append("pomarańcza")
    print(fruits)

    fruits[1] = "jagoda"
    print(fruits)

@task_separator
def task7():
    """Niemutowalność krotki:
Utwórz krotkę punkt = (10, 20, 30) .
Spróbuj zmienić pierwszy element krotki на 15 .
Wyjaśnij w komentarzu do kodu, dlaczego wystąpił błąd."""

    point = (10, 20, 30)
    print(point)

    print(
    '''
point[0] = 15
TypeError: 'tuple' object does not support item assignment

Krotki są niemutowalne, co oznacza, że po ich utworzeniu nie można zmieniać ich zawartości.
Są one używane do przechowywania danych, które nie powinny być modyfikowane, co zapewnia bezpieczeństwo i integralność danych.'''
    )

@task_separator
def task8():
    """Rzutowanie typów: Utwórz zmienną liczba_str = "5.8" . Przekonwertuj ją najpierw na
float , a następnie na int i wyświetl wyniki obu konwersji. Co zauważyłeś podczas
konwersji float na int ?"""

    liczba_str = "5.8"
    print(f"Original string: {liczba_str} of type {type(liczba_str)}")

    liczba_float = float(liczba_str)
    print(f"Converted to float: {liczba_float} of type {type(liczba_float)}")

    liczba_int = int(liczba_float)
    print(f"Converted to int: {liczba_int} of type {type(liczba_int)}")

    print(
'''
    Podczas konwersji float na int, liczba została zaokrąglona w dół do najbliższej liczby całkowitej.
    W tym przypadku 5.8 zostało przekonwertowane na 5, ponieważ int() obcina część dziesiętną, a nie zaokrągla.
''')

@task_separator
def task9():
    """Bramki logiczne: Napisz program, który poprosi o dwie wartości logiczne ( True lub
False ). Niech użytkownik wprowadza 1 dla True i 0 dla False . Program powinien
wyświetlić wyniki operacji AND oraz OR dla tych dwóch wartości."""

    while True:
        try:
            val1 = bool(int(input("Enter the first boolean value (1 for True, 0 for False):\n")))
            val2 = bool(int(input("Enter the second boolean value (1 for True, 0 for False):\n")))
        except ValueError:
            print("Invalid input. Please enter 1 or 0.")
            continue
        break

    print(f"{val1} AND {val2} = {val1 and val2}")
    print(f"{val1} OR {val2} = {val1 or val2}")
    

@task_separator
def task10():
    """Mini-projekt "Formater danych": Napisz program, który poprosi użytkownika o jego imię i
nazwisko w jednej linii (np. " jan kowalski "). Program powinien:
Oczyścić zbędne białe znaki.
Sprawić, aby każde słowo zaczynało się wielką literą (metoda .title() ).
Wyświetlić sformatowane dane oraz ich długość."""

    
    full_name = input("Enter your first and last name in one line:\n")

    full_name = full_name.strip()
    full_name = full_name.title()

    print(f"Formatted name: {full_name}")
    print(f"Length of formatted name: {len(full_name)}")


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
