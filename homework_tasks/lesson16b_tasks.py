"""Homework for lesson 12"""

from functools import wraps
from dataclasses import dataclass  # Task 6
from typing import Optional  # Task 6


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
    """
    Dopasuj pojęcia: Połącz w pary metodę HTTP z jej głównym przeznaczeniem.
    GET
    POST
    DELETE
    PUT
    A. Usunięcie danych
    B. Pobranie danych
    C. Zastąpienie danych w całości
    D. Utworzenie nowych danych
    """

    answer="""
    A. Usunięcie danych - DELETE
    B. Pobranie danych - GET
    C. Zastąpienie danych w całości - PUT
    D. Utworzenie nowych danych - POST
    """
    print(answer)


@task_separator()
def task2():
    """
    Własnymi słowami: Wyjaśnij, jaka jest różnica między Klientem a Serwerem w
architekturze Klient-Serwer. Podaj po jednym przykładzie każdego z nich.
    """
    answer="""
    Klient to program, obsługiwany przez użytkownika, który wysyła żądania o dane - informacje
    Serwer to program pracujący w trybie ciągłym, oczekujący na połączenie z Klieantami i odpowiadający
    na wysyłane przez nie żądania.

    Przykłady:
    Terminale płatnicze w sklepie - System operatora bankowego
    Gra multiplayer - Host rozgrywki
    """
    print(answer)


@task_separator()
def task3():
    """
    Model żądania: Utwórz w Pythonie słownik, który będzie reprezentował żądanie GET w
celu pobrania listy wszystkich artykułów z adresu /api/articles . W nagłówkach dodaj
klucz Host z wartością my-blog.com .
    """

    get_dictionary = {
        "Start-Line":{"Method":"GET","Target":"/api/articles/","version": "HTTP/2"},
        "Headers":{"Host":"my-blog.com","User-Agent":"Mozilla/5.0 (Windows NT 10.0; rv:115.0) Gecko/20100101 Firefox/115.0","Content-Type": "application/json"},
        "Body": None,
        }
   

@task_separator()
def task4():
    """
    Pytanie teoretyczne: Kiedy otwierasz stronę google.com w przeglądarce, jaką
metodę HTTP najprawdopodobniej wysyła Twoja przeglądarka, aby wyświetlić stronę
główną?
    """

    answer="""
    Klient-przeglądarka wysyła do serwera metodę GET
    """
    print(answer)

@task_separator()
def task5():
    """
    Pytanie teoretyczne: Do której warstwy modelu TCP/IP należy protokół IP,
odpowiedzialny za znalezienie drogi do komputera docelowego?
    """
    answer="""
    IP (Internet Protocol) należy do warstwy internetowej (Internet Layer) tego modelu
    """
    print(answer)
    

@task_separator()
def task6():
    """
    Klasa Request : Napisz klasę w Pythonie o nazwie HttpRequest .
Konstruktor __init__ powinien przyjmować method , target oraz opcjonalnie
headers (słownik) i body (string).
Dodaj metodę display() , która będzie drukować sformatowane żądanie na konsoli w
czytelnej formie, np.:
--- HTTP Request ---
Method: GET
Target: /index.html
Headers:
Host: example.com
User-Agent: PythonClient/1.0
Body:
(empty)
--------------------
Przetestuj klasę, tworząc obiekt dla żądania POST z przykładowymi danymi.
    """
    # from dataclasses import dataclass
    # from typing import Optional

    @dataclass
    class HttpRequest():
        method: str
        target: str
        headers: Optional[dict]
        body: Optional[str]

        def display(self):
            print("--- HTTP Request ---")
            print(f"Method: {self.method.upper()}")
            print(f"Target: {self.target}")
            print("Headers:")
            for key, value in self.headers.items():
                 print(f"{key}: {value}")
            if self.body:
                 print(f"Body:\n{self.body}")
            print("--------------------")
            
   
    call = HttpRequest(
        "POST", "/blog/posts", 
            {
                "Host":"my-blog.com",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; rv:115.0) Gecko/20100101 Firefox/115.0",
                "Content-Type": "application/json"
            },
            "{'post_title':'First post','content':'This is the first post on new blog page.'}"
            )
    call.display()


@task_separator()
def task7():
    """
    Parser URL: Napisz funkcję parse_url(url: str) -> dict , która przyjmuje jako
argument adres URL w formie stringa (np.
https://api.example.com:8080/users/search?active=true ) i zwraca słownik
zawierający jego części: protocol , domain , port i path .
Dla podanego przykładu, wynik powinien być: {'protocol': 'https', 'domain':
'api.example.com', 'port': 8080, 'path': '/users/search?active=true'} .
Obsłuż przypadek, gdy port nie jest podany (dla http domyślny to 80, dla https 443).
Wskazówka: Użyj metod do manipulacji stringami, takich jak split() czy find() .
    """

    def parse_url(url: str) -> dict:
        keys = ('protocol', 'domain', 'port', 'path')
        parsed = dict.fromkeys(keys)
        
        # PROTOCOL
        parse = url.split("://")
        parsed.update({keys[0]:parse[0].lower()})

        # DOMAIN and PORT
        parse = parse[1].split("/", 1)
        domain = parse[0].split(":")

        # Domain
        parsed.update({keys[1]:domain[0]})
        
        # Port
        if len(domain) == 1:
            parsed.update({keys[2]:80} if parsed.get(keys[0]) == "http" else {keys[2]:443})
        else:
            parsed.update({keys[2]:int(domain[1])})

        # PATH
        parsed.update({keys[3]:f"/{parse[1]}"})

        return parsed
    
    
    adress = "https://api.example.com:8080/users/search?active=true"
    adress2 = "https://www.skyshowtime.com/watch/playback/vod/SkyShowtime:"

    print(parse_url(adress))
    print(parse_url(adress2))


@task_separator()
def task8():
    """
    Symulacja Klient-Serwer: Stwórz prostą symulację interakcji Klient-Serwer przy użyciu
klas.
Napisz klasę FakeServer , która w __init__ tworzy "bazę danych" w postaci
słownika, np. self.db = {"users": [{"id": 1, "name": "Jan"}, {"id": 2,
"name": "Anna"}]} .

Klasa FakeServer powinna mieć metodę handle_request(request: dict) , która
analizuje żądanie (reprezentowane przez słownik).

Jeśli metoda to GET a cel to /users , powinna zwrócić słownik-odpowiedź z
kodem 200 i listą użytkowników w ciele.

Jeśli metoda to POST a cel to /users , powinna dodać nowego użytkownika z
ciała żądania do self.db i zwrócić odpowiedź z kodem 201 (Created).
Dla każdego innego żądania, zwróć odpowiedź z kodem 404 (Not Found).

Napisz klasę FakeClient z metodą send(server, request) , która "wysyła" żądanie
do obiektu serwera i drukuje otrzymaną odpowiedź.
Przetestuj scenariusze: pobranie wszystkich użytkowników, dodanie nowego
użytkownika i próbę dostępu do nieistniejącego zasobu.
    """
    @dataclass
    class FakeServer:
        db = {"users": [{"id": 1, "name": "Jan"}, {"id": 2,"name": "Anna"}]}

        def handle_request(self, request: dict) -> dict:
            if request.get("target") == "/users":
                if request.get("method") == "GET":
                    return {"Status-Line": "200 (OK)", "Body": self.db.get("users")}
                elif request.get("method") == "POST":
                    # new user
                    user = request.get("body")
                    # next id
                    next_id = len(self.db.get("users"))+1
                    # new record
                    user.update({"id": next_id})
                    # commit
                    self.db.get("users").append(user)
                    return {"Status-Line": "201 (Created)", "Body": None}
            else:
                return {"Status-Line": "404 (Not Found)", "Body": None}

        def server_get(self):
            user = {"name": "Kasia"}
            id = len(self.db.get("users"))+1
            user.update({"id": id})
            self.db.get("users").append(user)
            return self.db.get("users")
        
    
    class FakeClient:
        def send(server: object, request: dict):
           return server.handle_request(request)

    
    req1 = {"method": "GET", "target": "/users", "body": None}
    req2 = {"method": "POST", "target": "/users", "body":{"name": "Kasia"}}
    req3 = {"method": "GET", "target": "/location", "body": None}
    adress = FakeServer()

    print(f"Try GET:\n{FakeClient.send(adress, req1)}\n")
    print(f"Try POST:\n{FakeClient.send(adress, req2)}\n")
    print(f"Results: {adress.db}\n")
    print(f"Try GET with  access a non-existent resource:\n{FakeClient.send(adress, req3)}")
        

@task_separator()
def task9():
    """
    PUT vs PATCH: Wyobraź sobie, że na serwerze pod adresem /users/1 znajduje się
następujący zasób w formacie JSON: {"name": "Katarzyna", "email":
"k.nowak@example.com", "city": "Warszawa"} .
Opisz, jak wyglądałoby ciało żądania PUT , aby zmienić tylko imię na "Kasia".
Opisz, jak wyglądałoby ciało żądania PATCH , aby zmienić tylko imię na "Kasia".
Wyjaśnij w komentarzu w kodzie, dlaczego te żądania się różnią i która metoda jest
bardziej "oszczędna" pod względem przesyłanych danych.
    """
    answer="""
    Metoda PUT przekazuje całość danych zawierających elementy do zmiany, w tym przypadku cały słownik.
    Jeśli dane okazałyby sięże są niekompletne, to brakujące elementy zostaną zastąpione wartościami domyślnymi,
    a jeśli takich nie ma, to oryginalne wartości zostaną usunięte.

    Metoda PATCH przekazuje tylko te elementy, które mają być zmienione i nie wchodzi w interakcję z pozostałymi.
    Oznacza to, że do przesłania jest mniej danych - dokładnie tyle ile ma ulec zmianie. W tym przypadku
    jest to tylko {"name": "Katarzyna"} oraz adres '/users/1' wskazujący miejsce zmian i nie ma to
    dużego znaczenia, jednak może być istotne przy dużych zakresach danych lub przy znaczącej liczbie
    połączeń Klient-Serwer.
    """
    print(answer)
    
    
@task_separator()
def task10():
    """
    Walidator nagłówków: Napisz funkcję validate_request(request_dict: dict) ,
która sprawdza, czy w słowniku reprezentującym żądanie HTTP znajdują się kluczowe
nagłówki: Host i User-Agent .
Jeśli któregoś z nagłówków brakuje w kluczu headers , funkcja powinna podnieść
wyjątek ValueError z odpowiednim komunikatem (np. "Brak wymaganego nagłówka:
Host").Użyj bloku try...except , aby przetestować działanie funkcji z poprawnym i
niepoprawnym słownikiem żądania. To ćwiczenie łączy wiedzę o sieciach z obsługą
wyjątków.
    """

    def validate_request(request_dict: dict):
        headers = ('method', 'adress','Host', 'User-Agent', 'Content-Type', 'Content')
        for header in headers:
            if not header in list(request_dict.keys()):
                raise ValueError(f"Brak wymaganego nagłówka: {header}")
        return "Nagółówki poprawne"

    # All Headers included
    call1 ={
        "method": "POST",
        "adress": "/blog/posts",
        "Host":"my-blog.com",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; rv:115.0) Gecko/20100101 Firefox/115.0",
        "Content-Type": "application/json",
        "Content": "{'post_title':'First post','content':'This is the first post on new blog page.'}",
        }
    
    # Missing Host Header
    call2 ={
        "method": "POST",
        "adress": "/blog/posts",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; rv:115.0) Gecko/20100101 Firefox/115.0",
        "Content-Type": "application/json",
        "Content": "{'post_title':'First post','content':'This is the first post on new blog page.'}",
        }
    
    # Missing User-Agent Header
    call3 ={
        "method": "POST",
        "adress": "/blog/posts",
        "Host":"my-blog.com",
        "Content-Type": "application/json",
        "Content": "{'post_title':'First post','content':'This is the first post on new blog page.'}",
        }
    
    cases = [
        lambda: validate_request(call1),  # All Headers included
        lambda: validate_request(call2),  # Missing Host Header
        lambda: validate_request(call3),  # Missing User-Agent Header
        ]

    # Try cases
    oper = 0
    while len(cases) > oper:
        try:
            print(cases[oper]())
        except ValueError as e:
            print(f"Error {e}")
        finally:
            oper += 1


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
 