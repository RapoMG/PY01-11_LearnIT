"""Homework for lesson """

from functools import wraps


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
    """Klasa Film
Stwórz klasę Film, która przy tworzeniu obiektu będzie przyjmować tytul, rezyser i
rok_produkcji. Dodaj metodę informacje(), która będzie zwracać string z pełnymi
informacjami o filmie w formacie: "Tytuł" (rok_produkcji), reżyseria: Reżyser. Stwórz dwa
obiekty tej klasy i wydrukuj informacje o nich."""

    class Film:
        def __init__(self, tittle: str, director: str, date: int):
            self.tittle = tittle
            self.director = director
            self.date = date

        def information(self):
            return f"'{self.tittle}' ({self.date}), directed by {self.director}."
        
    movie1 = Film("Father Mother Sister Brother", "Jim Jarmusch ",2025)
    movie2 = Film("Star Wars", "George Lucas", 1977)

    print(movie1.information())
    print(movie2.information())


@task_separator()
def task2():
    """Atrybuty Produkt
Zdefiniuj klasę Produkt z konstruktorem init przyjmującym nazwa, cena i kategoria. Stwórz
obiekt tej klasy, a następnie wydrukuj każdy z jego atrybutów w osobnej linii."""

    class Produkt:
        """I am simple product, I do nothing, just lay here, waiting to be picked."""
        def __init__(self, name: str , price: float, category: str):
            self.name = name
            self.price = price
            self.category = category

    p = Produkt("Chrupki", 8.59, "PDK")

    print(p.name)
    print(p.price)
    print(p.category)


@task_separator()
def task3():
    """Dziedziczenie Pracownik -> Programista
Stwórz klasę bazową Pracownik z atrybutami imie i stawka_godzinowa. Dodaj metodę
oblicz_pensje(liczba_godzin). Następnie stwórz klasę potomną Programista, która
dziedziczy po Pracownik. W klasie Programista dodaj atrybut jezyki_programowania (lista
stringów). Stwórz obiekt klasy Programista i wywołaj na nim metodę oblicz_pensje."""

    class Employee:
        def __init__(self, name: str, hourly_rate: float):
            self.name = name
            self.hourly_rate = hourly_rate
        
        def salary(self, hours: float):
            return self.hourly_rate * hours
    
    class Programer(Employee):
        def __init__(self, name: str, hourly_rate: str, prog_languages: list[str]):
            super().__init__(name, hourly_rate)
            self.prog_languages = prog_languages

    
    emp1 = Programer("Wojciech", 35.50, ["Python",] )
    print(emp1.salary(90))


@task_separator()
def task4():
    """Czytelny Punkt
Stwórz klasę Punkt do reprezentowania punktu w 2D, z atrybutami x i y. Zaimplementuj
metodę str, aby print(punkt) wyświetlał współrzędne w formacie (x, y)."""

    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

        def point(self):
            return f"({self.x}, {self.y})"

    p1 = Point(6 , 8)
    print(p1.point())


@task_separator()
def task5():
    """Polimorficzna Figura
Stwórz klasę bazową Figura z metodą oblicz_pole(), która pass (nic nie robi). Następnie
stwórz dwie klasy potomne: Kwadrat (z atrybutem bok) i Kolo (z atrybutem promien). W obu
klasach nadpisz metodę oblicz_pole() odpowiednimi wzorami matematycznymi (dla koła
przyjmij PI=3.14159). Stwórz listę zawierającą jeden kwadrat i jedno koło, a następnie w
pętli wydrukuj pole każdej figury."""

    class Figure:
        def area(self):
            pass
    
    class Square(Figure):
        def __init__(self, side: float):
            super().__init__()
            self.side = side

        def area(self):
            return self.side ** 2
        
    class Circle(Figure):
        def __init__(self, radius: float):
            super().__init__()
            self.radius = radius
            self.pi = 3.14159

        def area(self):
            return self.pi * (self.radius ** 2)
        
    
    figs = [Square(3), Circle(4.2)]

    for fig in figs:
        print(fig.area())

@task_separator()
def task6():
    """Wektor 2D i przeciążanie operatorów
Stwórz klasę Wektor2D z atrybutami x i y. Przeciąż następujące operatory:
__add__(self, other) : do dodawania dwóch wektorów (dodajemy odpowiadające
sobie współrzędne).
__sub__(self, other) : do odejmowania wektorów.eq(self, other): do porównywania, czy dwa wektory są równe (mają te same x i y).
Dodatkowo zaimplementuj str do ładnego wyświetlania. Przetestuj działanie, tworząc
dwa wektory i wykonując na nich wszystkie zaimplementowane operacje."""

    class Vector2D:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

        def __add__(self, other: object):
            return Vector2D(self.x + other.x, self.y + other.y)
        
        def __sub__(self, other: object):
            return Vector2D(self.x - other.x, self.y - other.y)
        
        def __eq__(self, other: object):
            if self.x == other.x and self.y == other.y:
                return "Vectors are equal to each other."
            else:
                return "Vectors are not equal to each other."
            
        def __str__(self):
            return f"Vector ({self.x}, {self.y})"

    
    v1 = Vector2D(7, 6)
    v2 = Vector2D(6, 4)

    v_add = v1.__add__(v2)
    print(v_add.__str__())

    v_sub = v1.__sub__(v2)
    print(v_sub.__str__())

    v_neq = v1.__eq__(v2)
    print(v_neq)

    v3= Vector2D(7, 6)

    v_eq = v1.__eq__(v3)
    print(v_eq)
    

@task_separator()
def task7():
    """Enkapsulacja w Telewizorze
Stwórz klasę Telewizor. Użyj enkapsulacji, aby ukryć następujące atrybuty: kanal
(domyślnie 1), glosnosc (domyślnie 10), __wlaczony (domyślnie False). Stwórz publiczne
metody do zarządzania telewizorem:
wlacz() i wylacz()
zmien_kanal(numer) : kanał można zmienić tylko, gdy TV jest włączony.
glosniej() i ciszej() : głośność można regulować w zakresie 0-100 i tylko, gdy TV
jest włączony.
info(): wyświetla aktualny stan (włączony/wyłączony, kanał, głośność). Przetestuj, czy
nie da się zmienić kanału na wyłączonym telewizorze lub ustawić głośności powyżej
100. """
    
    class Televisor:
        def __init__(self):
            self.__chanel = 1
            self.__volume = 10
            self.__turned_on = False

        def turn_on(self):
            self.__turned_on = True
            return "Televisor is turned on."

        def turn_off(self):
            self.__turned_on = False
            return "Televisor is turned off."

        def set_chanel(self, ch: int):
            if self.__turned_on:
                self.__chanel = ch
                return f"Current chanel: {self.__chanel}."
            else:
                return "Can't change chanel: televisor is turned off."

        def volume_up(self):
            if self.__turned_on:

                if self.__volume < 100:
                    self.__volume += 1

                return f"Current volume: {self.__volume}."
            
            else:
                return "Can't incress volume: televisor is turned off."

        def volume_down(self):
            if self.__turned_on:

                if self.__volume > 0:
                    self.__volume -= 1

                return f"Current volume: {self.__volume}."
            
            else:
                return "Can't decress volume: televisor is turned off."
            
        def user_info(self):
            if self.__turned_on:
               return f"Televisor turned on: {self.__turned_on}, chanel {self.__chanel}, volume {self.__volume}."
            
            else:
                return "Can't display info: televisor is turned off."

        def info(self):
            return f"Diagnostics:\nTelevisor turned on: {self.__turned_on}, chanel {self.__chanel}, volume {self.__volume}."
        
    
    tv = Televisor()

    pseudo_tests = [
        tv.volume_up(),
        tv.volume_down(),
        tv.set_chanel(22),
        tv.user_info(),
        tv.info(),
        tv.turn_on(),
        tv.volume_up(),
        tv.volume_up(),
        tv.volume_down(),
        tv.set_chanel(25),
        tv.user_info(),
        tv.turn_off(),
        ]
    
    for test in pseudo_tests:
        print(test)

    tv.turn_on()
    print("\nBoundary volume values:")

    tv._Televisor__volume = 100
    print(tv.volume_up())
    
    tv._Televisor__volume = 0
    print(tv.volume_down())


@task_separator()
def task8():
    """Hierarchia instrumentów muzycznych
Zaprojektuj hierarchię klas: Instrument -> Strunowy i Dety. Następnie Gitara (dziedziczy po
Strunowy) i Trabka (dziedziczy po Dety). Klasa Instrument powinna mieć metodę graj(),
która zwraca ogólny komunikat. Każda kolejna klasa w hierarchii powinna nadpisywać tę
metodę, dodając coś od siebie i wywołując wersję z klasy nadrzędnej za pomocą
super().graj().
Instrument.graj() -> "Wydaje dźwięk."
Strunowy.graj() -> "Wydaje dźwięk. [Szarpnięcie struny]"
Gitara.graj() -> "Wydaje dźwięk. [Szarpnięcie struny] [Akord G-dur]" ."""
    
    class Instrument:
        def play(self):
            return "Plays sounds"

    class StringInstr(Instrument):
        def play(self):
            return f"{super().play()} by plucking strings"

    class WindInstr(Instrument):
        def play(self):
            return f"{super().play()} by blowing air"

    class Guitar(StringInstr):
        def play(self):
            return f"{super().play()} in G major chord."

    class Trumpet(WindInstr):
        def play(self):
            return f"{super().play()} in G major scale."
    

        
    g = Guitar()
    print(g.play())

    t = Trumpet()
    print(t.play())
    

@task_separator()
def task9():
    """Walidacja danych w init
Stwórz klasę RejestracjaUzytkownika. W konstruktorze init przyjmuj email i haslo.
Wewnątrz konstruktora dodaj walidację:
Sprawdź, czy email zawiera znak @ . Jeśli nie, podnieś wyjątek ValueError z
odpowiednim komunikatem.
Sprawdź, czy haslo ma co najmniej 8 znaków. Jeśli nie, podnieś ValueError. Użyj bloku
try...except, aby przetestować tworzenie obiektów z poprawnymi i niepoprawnymi
danymi."""

    class UserRegistration:
        def __init__(self, email: str, password: str):
            if len(password) < 8:
                raise ValueError ("Password too short")
            else:
                self.password = password

            if not "@" in email:
                raise ValueError ("No @ character in mail address")
            else:
                self.email = email
        
        def __str__(self):
            return f"email: {self.email}, password: {self.password}"


    # Valid arguments
    try:
        a = UserRegistration("test@example.com", "asdfghjk")
        print(a.__str__())
    except ValueError as e:
        print(f"Error {e}")

    # Invalid password argument
    try:
        b = UserRegistration("test@example.com", "asdf")
        print(b.__str__())
    except ValueError as e:
        print(f"Error {e}")    
    
    # Invalid Email argument
    try:
        c = UserRegistration("testexample.com", "asdfghjk")
        print(c.__str__())
    except ValueError as e:
        print(f"Error {e}")

    

@task_separator(True)
def task10():
    """Eksploracja MRO
Stwórz następującą, złożoną hierarchię dziedziczenia:
class A
class B(A)
class C(A)class D(B)
class E(C)
class F(D, E) Narysuj schemat tej hierarchii w mermaid. Następnie, nie uruchamiając
kodu, spróbuj przewidzieć, jakie będzie MRO dla klasy F. Na koniec sprawdź swoją
odpowiedź, używając print(F.mro()). """

    import mermaid as md
    from mermaid.statediagram import State,StateDiagram,Transition
        
    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B):
        pass

    class E(C):
        pass

    class F(D, E):
        pass
   
    
    #  My template for mermaid-py
    """
    import mermaid as md
    from mermaid.statediagram import State,StateDiagram,Transition,Start,End

    states = [Start(),State('Still'),State('Moving'),State('Crash'),End()]
    
    transitions = [
    Transition(to=states[1]),
    Transition(from_=states[1]),
    Transition(states[1],states[2]),
    Transition(states[2],states[1]),
    Transition(states[2],states[3]),
    Transition(from_=states[3])
    ]

    diagram = StateDiagram('test diagram',states,transitions)
    
    md.Mermaid(diagram).to_png("diagram.png")
    """

    states = [
        State('Class A'), 
        State('Class B'),
        State('Class C'),
        State('Class D'),
        State('Class E'),
        State('Class F'),
        ]

    transitions = [
    Transition(states[0],states[1]),  # A -> B
    Transition(states[0],states[2]),  # A -> C
    Transition(states[1],states[3]),  # B -> D
    Transition(states[2],states[4]),  # C -> E
    Transition(states[3],states[5]),  # D -> F
    Transition(states[4],states[5]),  # E -> F
    ]

    diagram = StateDiagram('Class MRO diagram',states,transitions)
    
    md.Mermaid(diagram).to_svg("L10_task10_diagram.svg")
    
    prediction = """
    If you think about this classes inheritage as layers,
    then MRO should follow objects layer by layer.

    For Class F, the first parent is Class D, and second is Class E.
    This means next in line will be Class B (parent of Class D),
    and then Class C. The last will be Class A (parrent of B and C).
    Of course, there's a Class Object - parent of Class A, and 'template'
    for all created classes.
    """
    print(prediction)

    print(F.mro())

    correct = """
    I was wrong! MRO Doesn't track 'layers' but 'lines' of parents.
    So it's F -> D -> B as one line, then E -> C, and finally A as top class.
    (And the class object next, of course)
    """
    print(correct)


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
 