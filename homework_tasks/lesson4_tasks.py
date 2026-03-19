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
    """Mini-kalkulator: Napisz program, który prosi użytkownika o podanie dwóch liczb, a
następnie wyświetla wynik ich dodawania, odejmowania, mnożenia i dzielenia. Pamiętaj o
konwersji typów z input() ."""

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue
        break

    print(f"{num1} + {num2} = {num1 + num2}")
    print(f"{num1} - {num2} = {num1 - num2}")
    print(f"{num1} * {num2} = {num1 * num2}")

    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Cannot divide by zero.")

@task_separator
def task2():
    '''Identyfikator obiektu: Utwórz trzy zmienne ( a , b , c ) z tą samą wartością 256 . Sprawdź
i wyświetl ich id() . Następnie utwórz trzy zmienne z wartością 257 i również sprawdź ich
id() . Czy widzisz różnicę w zachowaniu Pythona? Wyjaśnij dlaczego w komentarzu.'''

    a = 256
    b = 256
    c = 256

    print(f"ID of a: {id(a)}")
    print(f"ID of b: {id(b)}")
    print(f"ID of c: {id(c)}")

    x = 257
    y = 257
    z = 257

    print(f"ID of x: {id(x)}")
    print(f"ID of y: {id(y)}")
    print(f"ID of z: {id(z)}")

    print("""
          In Python, small integers (typically from -5 to 256) are interned, meaning they are stored in memory only once
          and all variables with that value point to the same object. Therefore, a, b, and c have the same id().
          However, integers larger than 256 are not interned, so x, y, and z are different objects in memory,
          resulting in different id() values. 
          However, since Python 3.7, the behavior of interning may vary based on implementation and optimizations,
          so it's not guaranteed for all integers above 256.
    """)

@task_separator
def task3():
    '''Porównanie is vs == : Utwórz dwie różne listy lista1 = [1, 1] i lista2 = [1, 1] .
Sprawdź wynik porównania lista1 is lista2 oraz lista1 == lista2 . Wyświetl wyniki
i w komentarzu wyjaśnij, dlaczego są różne.'''

    lista1 = [1, 1]
    lista2 = [1, 1]

    print(f"lista1 is lista2: {lista1 is lista2}")
    print(f"lista1 == lista2: {lista1 == lista2}")

    print("""
          The 'is' operator checks for identity, meaning it checks if both operands refer to the same object in memory.
          Since lista1 and lista2 are two different list objects, 'lista1 is lista2' returns False.
          The '==' operator checks for equality, meaning it checks if the contents of the lists are the same.
          Since both lists contain the same elements [1, 1], 'lista1 == lista2' returns True.
    """)


@task_separator
def task4():
    '''Formatowanie print() : Napisz program, który wyświetli listę zakupów:
"jajka,mleko,chleb" . Użyj funkcji print() z trzema argumentami tekstowymi i
odpowiednio ustawionym parametrem sep .'''

    print("jajka", "mleko", "chleb", sep=",")


@task_separator
def task5():
    '''Wejście w jednej linii: Użyj funkcji print() i jej parametru end , aby zadać pytanie i
pozwolić użytkownikowi odpowiedzieć w tej samej linii. Przykład: Podaj swoje imię:
[tutaj użytkownik wpisuje] .'''

    print("Enter your name: ", end="")
    name = input()
    print(f"Hello, {name}!")


@task_separator
def task6():
    '''Prawda czy fałsz?: Napisz program, który prosi użytkownika o wpisanie dowolnego tekstu.
Następnie, używając konwersji na bool , sprawdź, czy wpisany tekst jest "prawdziwy"(niepusty) i wyświetl odpowiedni komunikat.'''

    user_input = input("Enter any text: ")
    if bool(user_input):
        print("The entered text is true (not empty).")
    else:
        print("The entered text is false (empty).")


@task_separator
def task7():
    '''Błąd konwersji: Napisz program, który świadomie spróbuje przekonwertować słowo
"Python" na liczbę całkowitą. Uruchom go, zobacz błąd ValueError , a następnie
"napraw" program, umieszczając błędną linię w komentarzu i dodając wyjaśnienie, dlaczego
kod nie działał.'''

    print("""
    # The following line will raise a ValueError because "Python" cannot be converted to an integer.
    # int("Python")""")

    print("""
        The code above is commented out because it raises a ValueError. 
        The string 'Python' cannot be converted to an integer, which is why the code does not work.
    """)


@task_separator
def task8():
    '''Obliczanie wieku psa: Przyjmuje się, że pierwszy rok życia psa to 15 ludzkich lat, drugi to
9, a każdy kolejny to 5. Napisz program, który pyta o wiek psa w latach, a następnie oblicza
i wyświetla jego wiek w "ludzkich" latach.'''

    while True:
        try:
            dog_age = int(input("Enter the dog's age in years: "))
            if dog_age < 0:
                print("Age cannot be negative. Please enter a valid age.")
                continue
            break
        except ValueError:
            print("Please enter a valid integer for the dog's age.")
            continue

    if dog_age == 0:
        human_age = 0
    elif dog_age == 1:
        human_age = 15
    elif dog_age == 2:
        human_age = 24
    else:
        human_age = 24 + (dog_age - 2) * 5

    print(f"The dog's age in human years is: {human_age}")


@task_separator
def task9():
    '''Identyfikator po zmianie: Utwórz zmienną x = 10 . Wyświetl jej id() . Następnie
przypisz do x nową wartość x = x + 1 . Ponownie wyświetl id() . Czy identyfikator się
zmienił? Dlaczego? Odpowiedz w komentarzu.'''

    x = 10
    print(f"ID of x before change: {id(x)}")

    x = x + 1
    print(f"ID of x after change: {id(x)}")

    print("""
          The ID of x changed because integers in Python are immutable. When we perform the operation x = x + 1, 
          a new integer object is created with the value 11, and x now references this new object. 
          The original integer object with the value 10 remains unchanged in memory, and its ID is different from the new object.
    """)
    

@task_separator
def task10():
    '''Komentowanie kodu: Poniżej znajduje się fragment kodu. Dodaj do niego komentarze
jednoliniowe oraz docstring dla funkcji, wyjaśniając, co robi każda część.

    def oblicz_pole_prostokata(a, b):
        # Tutaj dodaj docstring

        # Tutaj dodaj komentarz
        pole = a * b

        # Tutaj dodaj komentarz
        return pole

    bok_a = 10
    bok_b = 20
    wynik = oblicz_pole_prostokata(bok_a, bok_b)
    print(f"Pole prostokąta o bokach {bok_a} i {bok_b} wynosi {wynik}.")'''

    def oblicz_pole_prostokata(a, b):
        """Funkcja oblicza pole prostokąta na podstawie długości jego boków a i b."""
        
        # Obliczamy pole prostokąta mnożąc długość boku a przez długość boku b
        pole = a * b

        # Zwracamy obliczone pole
        return pole
    
    bok_a = 10
    bok_b = 20
    wynik = oblicz_pole_prostokata(bok_a, bok_b)
    print(f"Pole prostokąta o bokach {bok_a} i {bok_b} wynosi {wynik}.")


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
