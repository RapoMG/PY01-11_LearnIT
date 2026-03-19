"""Homework for lesson 8"""

from functools import wraps, reduce
from datetime import datetime
import inspect

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
    """Bezpieczny kalkulator: Napisz program, który w pętli prosi użytkownika o podanie dwóch
liczb i operacji ( + , - , * , / ). Zaimplementuj pełną obsługę błędów ValueError (gdy
dane nie są liczbami) i ZeroDivisionError . Dodaj blok else do wyświetlania wyniku i
finally z komunikatem "Kolejna operacja..."."""

    def calc(num1: float, num2: float, symbol: str):
        INF = chr(8723)+chr(32)+chr(8734)
        try:
            if symbol == "/":
                result = num1 / num2
            elif symbol == "*":
                result = num1 * num2
            elif symbol == "+":
                result = num1 + num2
            elif symbol == "-":
                result = num1 - num2
        
        # This should be improved. The return statement should send one data type to the caller.
        except ZeroDivisionError:
            return INF

        except Exception as e:
            return f"Error: {e}"
        
        else:
            return result
        
    def app():
        OPERATORS = ("/","*","-","+")
        END = ("q","quit","e","end")
        while True:
            try:
                number1 =  float(input("Podaj pierwszą liczbę:\n"))
                number2 =  float(input("Podaj drugą liczbę:\n"))                   
            
            except ValueError as e:
                print(f"{e}: wprowadzona wartość nie jest liczbą.\n")

            try:
                operator = input(f"Wpisz działanie do wykonania {' '.join(OPERATORS)}\n")
                if operator not in OPERATORS:
                    raise ValueError()
                
            except ValueError:
                print("Błędny symbol działania!\n")

            else:
                print(f"Wynik działania: {calc(number1, number2, operator)}\n")

            finally:
                end = input("Wpisz [q] aby zakończyć lub naciśnij [Enter] aby kontynuować\n")
                if end in END:
                    break
                print("Kolejna operacja...\n") 
    app()
    

@task_separator()
def task2():
    """Walidator wieku: Stwórz funkcję rejestruj_uzytkownika(wiek) , która rzuca własnym,
zdefiniowanym przez Ciebie wyjątkiem WiekNiepoprawnyError , jeśli wiek jest mniejszy niż
18. Napisz kod, który wywołuje tę funkcję i obsługuje ten wyjątek."""

    class IncorrectAgeError(Exception):
        """Error raised when age does not meet the criteria."""
        pass

    def register_user(age: int):
        if age < 18:
            raise IncorrectAgeError("Użytkownik niepełnoletni!") 
        return {"age": age}
    
    # Code
    try:
        age = int(input("Podaj wiek użytkownika :\n"))
        user_age = register_user(age)
        print(f"Data to add to the user record: {user_age}")
    except ValueError:
        print('Wiek musi być liczbą całkowitą:')
    except IncorrectAgeError as e:
        print(f'Rejestracja niemożliwa: {e}')


@task_separator()
def task3():
    """Czytanie pliku: Napisz funkcję, która próbuje otworzyć i odczytać plik o podanej nazwie.
Obsłuż wyjątki FileNotFoundError (gdy pliku nie ma) oraz PermissionError (gdy nie
ma uprawnień do odczytu)."""
    
    def read_only_opener(adress: str):
        """
        Opens file in read only mode.
        
        :param adress: path to a file
        :type adress: str
        """
        file = None  # to prevent error at "finally" if "try" skipped
        try:
            if adress:
                file = open(adress, "r")
                print(f"  ##### File Contents #####\n {file.read()}\n  ########## End ##########")
        except FileNotFoundError:
            print(f"No such file at this path:\n   {adress}")
        except PermissionError:
            print("You don't have permission to open this file")
        finally:
            if file:
                file.close()

    
    path_ = "txt.txt"
    read_only_opener(path_)
        

@task_separator()
def task4():
    """Asercja w funkcji: Stwórz funkcję oblicz_srednia(lista_ocen) , która zwraca średnią z
listy. Użyj assert , aby upewnić się, że przekazana lista nie jest pusta."""

    # from functools import reduce

    def grade_point_average(grades: list):
        avr = None

        try:
            assert len(grades) > 0, "No elements in passed list." 
            avr = reduce(lambda accu, grade: accu + grade, grades) / len(grades)
            avr = round(avr, 2)
        except AssertionError as e:
            print(f"{e} List cannot be empty.")
        except TypeError as e:
            print(f"{e} List contains elements other than 'int' or 'float'.")

        return avr
        

    students_grades = []
    print(f"Empty list execution: \n{grade_point_average(students_grades)}")

    students_grades2 = [6,3,1,]
    print(f"List {students_grades2} execution: \n{grade_point_average(students_grades2)}")
    
@task_separator()
def task5():
    """Logowanie błędów: Zmodyfikuj zadanie 1. tak, aby każdy napotkany wyjątek (wraz z jego
treścią) był zapisywany do pliku log.txt , a program kontynuował działanie. Użyj bloku
finally , aby upewnić się, że plik z logami jest zawsze zamykany."""

    #from datetime import datetime

    def logger(error: str):
        log = 'log_task5.txt'

        try:
            file = open(log, "a")
            file.write(f"{datetime.now()} - {error}")

        except FileNotFoundError:
            print(f"No log file exist, nor can it be created.")
        except PermissionError:
            print("You don't have permission to open this file")

        finally:
            if file:
                file.close()


    # This should be improved. The return statement should send one data type to the caller.
    def calc(num1: float, num2: float, symbol: str):
        INF = chr(8723)+chr(32)+chr(8734)
        try:
            if symbol == "/":
                result = num1 / num2
            elif symbol == "*":
                result = num1 * num2
            elif symbol == "+":
                result = num1 + num2
            elif symbol == "-":
                result = num1 - num2

        except ZeroDivisionError as e:
            logger(e)
            return INF

        except Exception as e:
            logger(e)
            return f"Error: {e}"
        
        else:
            return result
        
        
    def app():
        OPERATORS = ("/","*","-","+")
        END = ("q","quit","e","end")
        while True:
            try:
                number1 =  float(input("Enter the first number:\n"))
                number2 =  float(input("Enter the secound number:\n"))

            except ValueError as e:
                err = f"{e}: value in not a number.\n"
                logger(err)
                print(err)
                continue
            
            try:
                operator = input(f"Select operation to perform {' '.join(OPERATORS)}\n")
                if operator not in OPERATORS:
                    raise ValueError(operator)
                
            except ValueError as e:
                err = f"Incorrect operator: {e}\n"
                logger(err)
                print(err)

            else:
                print(f"Operation result: {calc(number1, number2, operator)}\n")

            finally:
                end = input("Enter [q] to quit or press [Enter] to continue\n")
                if end in END:
                    break
                print("Next operation...\n") 


    app()
    

@task_separator()
def task6():
    """Przerzucanie wyjątku: Napisz funkcję przetworz_dane(dane) , która w bloku
try...except łapie KeyError (np. przy próbie dostępu do nieistniejącego klucza w
słowniku), loguje go, a następnie rzuca ( raise ) nowy, własny wyjątek
BladPrzetwarzaniaDanychError z informacją, którego klucza brakowało."""

    #from datetime import datetime

    class DataProcessingError(Exception):
        "Raised when error occurs in process_data."

        # Keeps error data - good for debuging tools
        def __init__(self, missing_key, org_exeption: object):
            self.missing_key = missing_key
            self.org_exeption = org_exeption
            message = f"Missing required key: {missing_key}"
            super().__init__(message)
        

    def logger(error: str):
        log = 'log_task6.txt'

        try:
            time = datetime.now().isoformat(timespec="seconds")
            with open(log, "a", encoding="utf-8") as file:
                file.write(f"{time} - {error}\n")

        except PermissionError:
            print("You don't have permission to open this file")

        finally:
            if file:
                file.close()

    def process_data(data: dict):
        try:
            print(f"I pretend to be doing something important with dictionary item '{data['user']}'.")
            print(f"I pretend to be doing something different with dictionary item '{data['email']}'.")
            print(f"I pretend to be doing something different but still important with dictionary item '{data['age']}'.")
        except KeyError as e:
            missing_key = e.args[0]
            msg = f"Missing key '{missing_key}' in data dictionary."
            logger(msg)
            raise DataProcessingError(missing_key, e) from e  # 'from e' connects errors making easer to trace the source
        

    
    broken_dict = {"user": "FirstUser","age": 22, }
    #correct_dict = {"user": "FirstUser","email":"unknown@example.com","age": 22, }

    try:
        process_data(broken_dict)
    except DataProcessingError as e:
        print(f"Data processing error: {e}")


@task_separator()
def task7():
    """Bezpieczne pobieranie ze słownika: Napisz funkcję pobierz_wartosc(slownik,
klucz) , która bezpiecznie zwraca wartość dla danego klucza. Jeśli klucza nie ma, funkcja
nie powinna rzucać błędu, tylko zwracać None . Zrób to bez użycia try...except
(wskazówka: metoda .get() ). Następnie napisz drugą wersję z użyciem try...except
KeyError ."""
    
    # from datetime import datetime
    # import inspect

    def logger(error: str):
        log = 'log_task7.txt'

        try:
            time = datetime.now().isoformat(timespec="seconds")
            with open(log, "a", encoding="utf-8") as file:
                file.write(f"{time} - {error}\n")

        except PermissionError:
            print("You don't have permission to open this file")

        finally:
            if file:
                file.close()

    def get_value(data: dict):
        # call name of used function
        frame = inspect.currentframe()
        frame =  frame.f_code.co_name

        print(f"\nInside {frame}:\n")
        print(f"I pretend to be doing something important with dictionary item '{data.get('user')}'.")
        print(f"I pretend to be doing something different with dictionary item '{data.get('email')}'.")
        print(f"I pretend to be doing something different but still important with dictionary item '{data.get('age')}'.")
        
    def get_value_try(data: dict):
        # call name of used function
        frame = inspect.currentframe()
        frame =  frame.f_code.co_name

        print(f"\nInside {frame}:\n")
        try:
            print(f"I pretend to be doing something important with dictionary item '{data.get('user')}'.")
            print(f"I pretend to be doing something different with dictionary item '{data.get('email')}'.")
            print(f"I pretend to be doing something different but still important with dictionary item '{data.get('age')}'.")
        
        # KeyError wont be raised with .get() - safe acces
        except KeyError as e:
            missing_key = e.args[0]
            msg = f"Missing key '{missing_key}' in data dictionary."
            logger(msg)

    
    broken_dict = {"user": "FirstUser","age": 22, }
    # correct_dict = {"user": "FirstUser","email":"unknown@example.com","age": 22, }

    get_value(broken_dict)
    get_value_try(broken_dict)


@task_separator()
def task8():
    """Walidacja hasła v2: Rozbuduj funkcję do walidacji hasła. Powinna ona zwracać listę
wszystkich błędów walidacji, zamiast rzucać wyjątkiem po pierwszym napotkanym
problemie. Jeśli lista błędów nie jest pusta, rzuć własnym wyjątkiem BladWalidacjiError ,
przekazując do niego tę listę."""
    
   
    class PasswordValidationError(Exception):
        """Exception risedwhen password don't meets expectation."""

        def __init__(self, errors: list):
            self.errors = errors
            super().__init__("Password validation failed.")

    def validate_password(password: str):
        errors = []
        
        if len(password) < 8:
            errors.append("Password is to short (at least 8 characters).")

        if not any(char.isdigit() for char in password):
           errors.append("Password must contain at least 1 digit.")

        if not any(char.isupper() for char in password):
           errors.append("Password must contain at least 1 capital letter.")

        if len(errors)>0:
            raise PasswordValidationError(errors)

        print("Password is valid.")
        
    try:
        validate_password("toshort")
    except PasswordValidationError as e:
        errors = "\n".join(e.errors) 
        print(f"Validation error: \n{errors}")


@task_separator()
def task9():
    """Kontekstowy menedżer with : Pokaż, jak instrukcja with open(...) as f: upraszcza
kod z zadania 3, eliminując potrzebę jawnego używania bloku finally do zamykania
pliku."""
    
    def read_only_opener_but_better(adress: str):
        """
        Opens file in read only mode.
        
        :param adress: path to a file
        :type adress: str
        """
        # file = None  # no need for that
        try:
            if adress:
                with open(adress, "r") as file:
                    print(f"  ##### File Contents ##### \n\n{file.read()}\n\n  ########## End ##########")
        except FileNotFoundError:
            print(f"No such file at this path:\n   {adress}")
        except PermissionError:
            print("You don't have permission to open this file")
        # no need for finally, open always call exit()

    
    path_ = "txt.txt"
    read_only_opener_but_better(path_)
    

@task_separator(True)
def task10():
    """ Mini-projekt: Sumator liczb z pliku: Napisz program, który:
a. Pyta użytkownika o nazwę pliku.
b. Otwiera plik i czyta go linia po linii.
c. Każdą linię próbuje przekonwertować na liczbę i dodać do sumy.
d. Ignoruje linie, których nie da się przekonwertować na liczbę (obsługa ValueError).
e. Obsługuje FileNotFoundError, jeśli plik nie istnieje.
f. Na końcu, w bloku finally, wyświetla obliczoną sumę (nawet jeśli wystąpiły błędy po
drodze)."""
    
    class DataSourceError(Exception):
        """Raised when input data cannot be accessed or read."""
        pass


    def file_reader(address: str) -> float | None:
        """
        Reads the file and sums the numbers in each line.     

        Returns:
            float: sum of numeric values
            None: if no valid numeric data was found
        Raises:
            DataSourceError: if the file cannot be opened
        """

        #open file
        total = 0.0
        math_lines = 0  # it will distinguish between the 0 value and no value.
        try:
            with open(address, "r") as file:
                while True:
                    try:
                        line = file.readline() # read line
                        if not line:
                            break  # stop at the end of the file
                        
                        total += float(line.strip()) # convert to float and add to the sum / strip removes spaces an and new line characters.
                        
                    except ValueError:
                        continue # not a number, skip

                    math_lines += 1
            
                # # Apparently, files are iterable in Python. With for loop don't need break.
                # for line in file:
                #     try:
                #         value = float(line) # read line
                #     except ValueError:
                #         continue # not a number, skip
            
                #     total += value  #outside try - no room for error here
                #     math_lines +=1

        except FileNotFoundError as e:
            raise DataSourceError(f"File {address} does not exist. Check spelling in the file name.") from e
            # Don't print here, it's not the user layer

        except PermissionError as e:
            raise DataSourceError(f"Restricted access to {address} file.") from e
        
        if math_lines == 0:
            return None
        
        return total  # Option: Return number of skipped lines - for entry data analysis


    def app() -> None:
        """
        Asks user to enter name of the file to be summed and presents the result as string.
        """

        file_name = input("\nEnter the name of the file to be summed:\n")
        # Option: Validation for empty name

        # call reader
        try:
            result = file_reader(file_name)
        
        except DataSourceError as e:
            print(f"Error ocurred: \n{e}")
            return  
            # Once return is executed, the function stops running, and any code written after it is ignored.
            # If no value is returned, Python automatically returns None.

        summary = "No data to sum up" if result is None else f"Total of the file is {result}"
        print(summary)


    while True:
        app()
        
        loop = input("Press [Enter] to read the next file, or type [e] to exit.\n")
        if loop.lower() == "e":
            break

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
 