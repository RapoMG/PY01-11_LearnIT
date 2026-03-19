"""Homework for lesson 7"""

from functools import reduce, wraps

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
   """Filtrowanie słów: Mając listę słów slowa = ["jabłko", "banan", "kiwi", "gruszka",
"truskawka"] , użyj list comprehension, aby stworzyć nową listę zawierającą tylko te
słowa, które mają więcej niż 5 liter."""
   words = ["jabłko", "banan", "kiwi", "gruszka","truskawka"]

   fil_words = [word for word in words if len(word) > 5]

   print(fil_words)

@task_separator()
def task2():
    """Sortowanie słownika: Masz słownik oceny = {"Jan": 4, "Anna": 5, "Piotr": 3,
"Kasia": 4} . Użyj funkcji sorted() i funkcji lambda, aby posortować elementy
słownika (klucz, wartość) według ocen (od najwyższej do najniższej)."""

    grades = {"Jan": 4, "Anna": 5, "Piotr": 3,"Kasia": 4}
    
    #                        lambda arguments : expression
    #sorted(iterable, key=A Function to execute to decide the order. Default is None, reverse=Boolean. Default is False) 
    sorted_by_grades = dict(sorted(grades.items(), key=lambda pair: pair[1],reverse=True))

    print(sorted_by_grades)

@task_separator()
def task3():
    """Konwersja na wielkie litery: Użyj funkcji map() , aby przekształcić listę imion imiona =
["anna", "piotr", "kasia"] w listę imion pisanych wielką literą."""
    names = ["anna", "piotr", "kasia"]

    # map() executes a specified function for each item in an iterable
    # map(The function to execute for each item, iterable) 
    title_names = list(map(lambda name: name.title(), names))

    print(title_names)

@task_separator()
def task4():
    """Znajdowanie liczb pierwszych: Użyj funkcji filter() , aby z listy liczb od 1 do 30 wybrać
tylko liczby pierwsze. (Wskazówka: napisz pomocniczą funkcję czy_pierwsza(n) , która
sprawdza, czy liczba jest pierwsza)."""

    numbers = list(range(1,31))

    def is_prime(num: int):
        divisor = 0

        # Check number of divisors for arg
        for _ in range(1, num+1):
            if num % _ == 0:
                divisor += 1
        
        # a prime number has exactly 2 divisors
        prime = divisor == 2

        return prime 

    # filter() returns an iterator where the items are filtered through a function to test if the item is acceptable (True)
    primes = list(filter(lambda number: is_prime(number), numbers ))

    print(primes)

@task_separator()
def task5():
    """ Iloczyn elementów: Użyj funkcji reduce() , aby obliczyć iloczyn (wynik mnożenia)
wszystkich liczb w liście [1, 2, 3, 4, 5] """

    # from functools import reduce

    numbers = list(range(1, 6))
    
    product = reduce(lambda x, y: x * y, numbers)

    print(product)


@task_separator()
def task6():
    """Licznik wywołań: Stwórz domknięcie (closure). Napisz funkcję stworz_licznik() , która
zwraca funkcję. Każde wywołanie zwróconej funkcji powinno zwiększać wewnętrzny licznik i
zwracać jego aktualną wartość."""

    def make_counter(start=0):
        counter = start
        def add_count(step=1):
            nonlocal counter
            counter += step
            return counter
        return add_count
    
    counting = make_counter()

    for _ in range(3):
        print(f" Function caled {counting()} time/s")
    


@task_separator()
def task7():
    """Dekorator logujący: Napisz dekorator @loguj , który przed wywołaniem udekorowanej
funkcji wypisze komunikat Uruchamiam funkcję [nazwa_funkcji]... , a po jej
zakończeniu Zakończono funkcję [nazwa_funkcji]."""
    def log(func):
        @wraps(func)
        def wrapper():
            title = func.__name__

            print(f"\nWszystkie stanowiska, czerwony alarm! \nWykonać funkcję {title}\n")
            result = func()
            print(f"Funkcję {title} wykonano. \nOdwołać alarm!\n")

            return result

        return wrapper

    @log
    def message():
        print("Mówi kapitan Picard, to jest nawiązanie do Star Trecka.\n")

    message()

@task_separator()
def task8():
    """Łączenie map i filter: Mając listę liczb [-5, 2, 8, -1, 0, 10] , użyj filter do
wybrania tylko liczb dodatnich, a następnie map do obliczenia ich kwadratów. Zrób to w
jednej linijce."""
    numbers = [-5, 2, 8, -1, 0, 10]
    
    # map(func, iteratable)
    # filter(func, iteratable)
    pos_square = list(map(lambda n: n ** 2, filter(lambda n: n > 0, numbers)))

    print(pos_square)


@task_separator()
def task9():
    """Dekorator z argumentem: Stwórz dekorator @powtorz(n) , który przyjmuje argument n i
powoduje, że udekorowana funkcja zostanie wykonana n razy."""

    from functools import wraps  # it should be imported at the top of file, not here, of course 


    # Main body of the decorator, it takes argumets for decorator
    def repeat(times=1):
        """
        Repeats decorated function
        
        :param times: number of additional runs of decorated function *default* 1
        """
        
        # Wrapper takes decorated function
        def wrapper(func):

            # Call takes arguments of decorated function 
            @wraps(func)  # it copies the identity of the decorated function to the wrapper (reduces despair while debugging)
            def call(*args, **kwargs): # its universal for functions with and without arguments

                # default execution: decorator repeats function (prints x times) but returns only last result
                # good for function where last result matters (expected one) eg. to fetch data, to ensure written data to disk or file
                result = None
                
                for _ in range(times+1):
                    result = func(*args, **kwargs) 

                return result  # important e.g. for decorators stacking. Lack of direct return produces None at decorator putput.

                """
                # decorator repeats function (prints x times) and returns all results
                # good for function where all results matters eg. sampling temperature, statistic simulation 

                results = []
                
                for _ in range(times+1):
                    results.append(func(*args, **kwargs))
                
                return results
                """
                                
            return call

        return wrapper


    @repeat(2)  # decorates all instances of the function and takes argument for that decorator
    def stutter():
        print("Repeats it like a broken record...\n")

    # call function
    stutter()
    

@task_separator(True)
def task10():
    """ Mini-projekt: Przetwarzanie danych: Masz listę słowników reprezentujących
użytkowników:
Napisz jednolinijkowy kod (używając kombinacji filter , map lub list comprehension),
który zwróci listę imion aktywnych użytkowników, którzy mają 18 lat lub więcej, pisanych
wielkimi literami.
uzytkownicy = [
{"imie": "Jan", "wiek": 30, "aktywny": True},
{"imie": "Anna", "wiek": 17, "aktywny": False},
{"imie": "Piotr", "wiek": 25, "aktywny": True}"""
    
    users = [
{"name": "Jan", "age": 30, "active": True},
{"name": "Anna", "age": 17, "active": False},
{"name": "Piotr", "age": 25, "active": True},
    ]

    # filter legal adults and active users [filter(function , iterable ) ]
    # get names [map( function, iterator)]
    # convert to capital letters [.upper inside map]

    active_users = list(map(lambda name: name["name"].upper(), filter(lambda user: user["active"] and user["age"]>=18, users)))

    print(f"Users that meet the criteria: {active_users}")


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
 