"""Homework for lesson 12"""

from functools import wraps  # task 10
from dataclasses import dataclass  # task 1
from random import randint  # task 4
from time import sleep


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
    """Iterator zakresu: Stwórz własną klasę iteratora Zakres(start, stop, krok) , która
będzie działać podobnie do wbudowanej funkcji range() , pozwalając na iterację od
start do stop z określonym krokiem .
    """

    # from dataclasses import dataclass

    @dataclass
    class Zakres:
        start: int
        stop: int
        krok: int = 1

        def __iter__(self):
            return self
        
        def __next__(self):
            # value to return
            num = self.start
            # test range
            if num <= self.stop:
                # prepare next step   
                self.start += self.krok
                # return current step
                return num
            else:
                raise StopIteration

    for x in Zakres(1,5,2):
        print(x)


@task_separator()
def task2():
    """Generator plików: Napisz funkcję generatora czytaj_duzy_plik(nazwa_pliku) , która
będzie czytać duży plik linia po linii, używając yield , aby zwracać każdą linię osobno.
Dzięki temu program nie załaduje całego pliku do pamięci.
    """
   
    def czytaj_duzy_plik(nazwa_pliku):
        file = open(nazwa_pliku, "r", encoding="utf-8")
        for line in file:
            yield line.strip()
        file.close()
    
        
    file_to_open = czytaj_duzy_plik("lorem_ipsum")

    lines_to_print = 4

    for _ in range(lines_to_print):
        print(next(file_to_open))


@task_separator()
def task3():
    """Przepisanie pętli for : Przepisz poniższą pętlę na jej dokładny odpowiednik z while ,
iter() i next() , włącznie z obsługą wyjątku StopIteration .

    for char in "Python":
        print(char.upper()) 
    """

    text = iter("Python")

    while True:
        try:
            char = next(text)
            print(char.upper())
        except StopIteration:
            break


@task_separator()
def task4():
    """Generator liczb losowych: Napisz generator losowe_liczby(min_val, max_val,
ilosc) , który wygeneruje ilosc liczb losowych z podanego zakresu. Użyj modułu
random .
    """

    # from random import randint

    def losowe_liczby(min_val: int, max_val: int, ilosc: int):
        for _ in range(ilosc):
            print(randint(min_val, max_val))

    losowe_liczby(1,100,5)
 

@task_separator()
def task5():
    """Wyrażenie generatorowe: Masz listę stringów dane = ["1", "2", "abc", "3", "4"] .
Użyj wyrażenia generatorowego, a następnie funkcji sum() , aby obliczyć sumę tylko tych
elementów, które są cyframi.
    """

    dane = ["1", "2", "abc", "3", "4"]

    gen = (int(x) for x in dane if x.isnumeric())
    
    print(sum(gen))


@task_separator()
def task6():
    """Dekorator sprawdzający typy: Napisz dekorator @sprawdz_typy , który sprawdzi, czy
wszystkie argumenty przekazane do udekorowanej funkcji są typu int . Jeśli nie, powinienrzucić TypeError .
    """

    def sprawdz_typy(func):
        
        def wrapper(*args, **kwargs):            
            
            # test args
            for arg in args:
                if type(arg) is not int:
                    raise TypeError(f"Argument '{arg}' passed to the '{func.__name__}' funnction is not an integer type")
            
            # test kwargs
            for kwarg in kwargs.items():
                if type(kwarg[1]) is not int:
                    raise TypeError(f"Keyword argument {kwarg[0]}={kwarg[1]} passed to the '{func.__name__}' funnction is not an integer type")
            
            result = func(*args, **kwargs)

            return result
        
        return wrapper
    
    @sprawdz_typy
    def sum_ints(*args, secret=1):
        sum = 0
    
        for arg in args:
            sum += arg
        sum = sum * secret
        return sum
    
    # list different cases
    attempts =[
               lambda: sum_ints(1,3,5),
               lambda: sum_ints(1,"3",5),
               lambda: sum_ints(1,3,5, secret="3"),
               lambda: sum_ints(1,3,5, secret=3),
               ]

    # test all cases
    for att in attempts:
        try:
            result = att()
        except TypeError as e:
            print(e)
        else:
            print(result)

   
@task_separator()
def task7():
    """Fabryka loggerów: Stwórz fabrykę stworz_logger(typ) , która w zależności od
argumentu "konsola" lub "plik" zwraca obiekt loggera. Logger powinien mieć metodę
log(wiadomosc) . Wersja konsolowa drukuje na ekranie, a plikowa dopisuje do pliku
app.log .
    """

    class Logger:
        def log(self, entry):
            raise NotImplementedError


    class ConsoleLogger(Logger):
        def log(self, entry):
            print(f"Log info: {entry}\n")


    class FileLogger(Logger):
        def log(self, entry):
            with open("app.log", "a", encoding="utf-8") as f:
                f.write({entry})


    def stworz_logger(typ:str):
        """accepted args typ: 'plik', 'konsola' """
        if typ == "konsola":
            return ConsoleLogger()
        elif typ == "plik":
            return FileLogger()
        raise ValueError(f"Unknown type: {typ}")


    data = "2026-01-11 09:00:54 ERROR Database query timeout"

    print_log = stworz_logger("konsola")
    save_log = stworz_logger("plik")

    print_log.log(data)
    save_log.log(data)


@task_separator()
def task8():
    """Singleton w praktyce: Zaimplementuj wzorzec Singleton dla klasy
KonfiguracjaAplikacji , która przy pierwszym tworzeniu wczytuje dane z fikcyjnego
pliku. Sprawdź, czy przy drugim tworzeniu instancji dane nie są wczytywane ponownie.
    """

    class KonfiguracjaAplikacji:
        _instance = None
        config_dict = dict

        def __new__(mcls, *args, **kwargs):
            if mcls._instance is None:
                with open("lorem_ipsum", "r", encoding="utf-8") as f:
                    print(f.readline())
                    mcls._instance = super().__new__(mcls, *args, **kwargs)
                    print("Fake config data loaded.\n")
                    mcls.config_dict = {"settings" : True}
            else:
                print("No need to load data again.\n")
                return mcls._instance
            
        
    KonfiguracjaAplikacji()
    KonfiguracjaAplikacji()

    
@task_separator()
def task9():
    """Nieskończony generator: Napisz generator cykl_kolorow() , który w nieskończoność
będzie zwracał kolory z listy ["czerwony", "zielony", "niebieski"] w pętli. Przetestuj
go, pobierając 10 pierwszych wartości.
    """

    colours = ["czerwony", "zielony", "niebieski"]

    def cykl_kolorow(colours: list[str]):
        while True:
            for colour in colours:
                yield colour

    
    gen = cykl_kolorow(colours)

    repeats = 10

    for _ in range(repeats):
        print(next(gen))

 
@task_separator()
def task10():
    """Mini-projekt: Dekorator cache'ujący: Stwórz dekorator @cache , który będzie
przechowywał wyniki wywołań funkcji dla danych argumentów. Jeśli funkcja zostanie
ponownie wywołana z tymi samymi argumentami, dekorator powinien zwrócić zapamiętany
wynik, zamiast wykonywać funkcję ponownie. Użyj słownika do przechowywania cache.
Przetestuj na funkcji, która wykonuje wolne obliczenia.
    """
    #from time import sleep
    #from functools import wraps

    def cache(func):
        cache_dict = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            # convert kwargs to hashable type - tuple.
            # sorting will make it independent of the order in which arguments are supplied
            from_dict = tuple(sorted(kwargs.items()))

            # crate tuple to store for future reference
            elements = (*args, from_dict )            

            # If used previously
            if elements in cache_dict:
                print("\nArg already used. Returning the previous result:")
                return cache_dict.get(elements)
            
            # First occurence
            else:
                print("\nNew args. New calculations:")
                result = func(*args, **kwargs)
                cache_dict.update({elements: result})
                return result

        return wrapper
    

    @cache
    def slow_function_imitation(a, b ,c=10, d="Value:"):
        print("Function stars")
        # Pretend something complicated takes time
        sleep(2)
        result = a + b

        # Pretend something complicated takes time
        print("Midle part of the function")
        sleep(4)

        result = result * c

        # Pretend something complicated takes time
        sleep(2)
        print("Function ends")

        return f"{d}:{result}"


    print(slow_function_imitation(1,5,c=3,d = "Result:"))
    print(slow_function_imitation(2,7,5))
    print(slow_function_imitation(1,5,d = "Result:",c=3))


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
 