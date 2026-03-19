"""Homework for lesson 2"""

from this import s as this_text

def task_separator(func):
    def wrapper():
        line_l = '<<< '
        line_r = ' >>>'
        title = func.__name__

        try:
            title = title.replace("task", "task ")
        except:
            pass

        print(f"\n{line_l * 2} {title.upper()} {line_r * 2}\n")
        func()
    return wrapper

@task_separator
def task1():
   print('Mam na imię Krzysztof')
   print('Moje hobby to RPG, gry planszowe i utrudnianie sobie zadań domowych.')
   print('Uczę się Pythona, bo chciałbym zarabiać pisząc lub testując kod.')

@task_separator
def task2():
    name = input("Podaj swoje imię:\n").capitalize()
    age = int(input("Ile masz lat?\n"))
    city = input("Skąd jesteś?\n").title()
    
    cases = (2,3,4) # Declension of word "lat / lata"
    dec_word = ""

    dec_word = "lata" if age % 10 in cases and age > 15 else "lat"

    print(f"\nMasz na imię {name}, masz {age} {dec_word}, a twoja miejscowość to {city}.")


@task_separator
def task3():
    while True:
        try:
            side_a = input("Podaj długość boku A\n")
            side_a = float(side_a.replace(",","."))
            break
        except ValueError:
            continue
    while True:
        try:
            side_b = input("Podaj długość boku B\n")
            side_b = float(side_b.replace(",","."))
            break
        except ValueError:
            continue

    print(f"Obwód prostokąta o wymiarach {side_a} x {side_b} wynosi {(side_a+side_b)*2}")


@task_separator
def task4():
    """Używając funkcji ord() , znajdź i wyświetl kody liczbowe ASCII dla
pierwszej litery Twojego imienia (wielką i małą literą)."""

    name = input("Podaj imię:\n")
    c_letter = name[0].capitalize()
    s_letter =name[0].lower()

    print(f"Wartość ASCII dla litery {s_letter} to {ord(s_letter)}, a dla {c_letter} to {ord(c_letter)}.\n")


@task_separator
def task5():
    """Program prosi użytkownika o nazwę rasy ( "Elf" , "Krasnolud" itp.)
oraz klasę ( "Wojownik" , "Mag" ). Następnie wyświetla: Stworzono postać: [Rasa]
[Klasa]."""
    races = ("Elf" , "Krasnolud", "Człowiek", "Niziołek",)
    classes = ("Wojownik" , "Mag", "Łotr", "Tropiciel", "Kapłan",)

    print("Wybierz spośród dostępnych ras wpisując numer:")
    counter = 0
    for race in races:
        counter += 1
        print(f'{counter}. {race}', end="\t")

    #that should be a function
    while True:
        try:
            selection = int(input("\n"))
        except ValueError:
            print("Błędny numer")
            continue

        if selection in range(1, len(races)+1):
            race = races[selection-1]
            break
        else:
            print(f"Wybór spoza zakresu 1 - {len(races)}")

    print("Wybierz spośród dostępnych klas wpisując numer:")
    counter = 0
    for class_ in classes:
        counter += 1
        print(f'{counter}. {class_}', end="\t")

    
    while True:
        try:
            selection = int(input("\n"))
        except ValueError:
            print("Błędny numer")
            continue

        if selection in range(1, len(classes)+1):
            class_ = classes[selection-1]
            break
        else:
            print(f"Wybór spoza zakresu 1 - {len(classes)}")
    
    print(f"\nStworzono postać: {race} {class_}. Udanej gry!")




@task_separator
def task6():
    """Napisz program, który pyta, czy użytkownik ma prawo jazdy
( tak/nie ) i ile ma lat. Wyświetl True , jeśli użytkownik ma 18 lat lub więcej ORAZ ma
prawo jazdy. W przeciwnym razie wyświetl False """

    while True:
        selection  = input("Czy masz prawo jazdy (tak/nie)\n").lower()
        
        if selection == "tak":
            licence = True
            break
        elif selection == "nie":
            licence = False
            break
        else:
            print(f"{selection} nie jest dostępną odpowiedzią.\n")

    while True:
        age = input(f"\nPodaj wiek:\n")

        try:
            age = int(age)
            break
        except ValueError:
            print(f"{age} nie jest wartością liczbową!\n")

    criteria = licence and age >= 18

    print(f"\nSpełniono kryteria: {criteria}")


@task_separator
def task7():
    """venv :
Utwórz folder project_test .
Wewnątrz niego utwórz środowisko wirtualne venv .
Aktywuj je.
Wykonaj polecenie pip list , aby zobaczyć, że nie ma zainstalowanych bibliotek.
Dezaktywuj środowisko."""

    print("""
terminal commands:
          
    > mkdir project_test
    > cd project_test
    > python3 -m venv venv
    > source venv/bin/activate
    (venv) > pip list
    (venv) > deactivate
    > cd ..
    > rm -r project_test
          
""")

@task_separator
def task8():
    """Dla użytkowników VM) Nawigacja w Ubuntu:
Otwórz terminal w swojej maszynie Ubuntu.
Utwórz folder moj_pierwszy_projekt na pulpicie ( cd Desktop , a następnie mkdir
moj_pierwszy_projekt ).
Przejdź do tego folderu.
Utwórz wewnątrz pusty plik main.py poleceniem touch main.py .
Wyświetl zawartość folderu poleceniem ls ."""

    print("""
    terminal commands:
          
    > cd Desktop
    > mkdir my_first_project
    > cd my_first_project
    > touch main.py
    > ls
    > cd ..
    > rm -r my_first_project
          
    """)


@task_separator
def task9():
    """Zen w częściach: Wyświetl na ekranie tylko pierwsze dwie linijki z "Zenu Pythona".
Wskazówka: musisz pobrać cały tekst i przetworzyć go jako ciąg znaków lub listę."""

    # from this import s as this_text
 
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)

    text = ("".join([d.get(c, c) for c in this_text])).split("\n")


    for _ in range(2):
        print(text[_+2])
        

@task_separator
def task10():
    """Mini-projekt "Konwerter Temperatury": Napisz program, który poprosi użytkownika o
temperaturę w stopniach Celsjusza, przekonwertuje ją na stopnie Fahrenheita według
wzoru F = C * 9/5 + 32 i wyświetli wynik z wyjaśnieniem."""

    while True:
        try:
            cel = float(input("Enter Celsius value to convert it to the Farenheit:\n"))
        except:
            continue

        far = cel * 9/5 + 32

        print(f"\nTemperature in FarenHeit is {far} degres\n")
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
