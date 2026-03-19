"""Homework for lesson 1"""

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
    print("Hello, cruel world!")

@task_separator
def task2():
    name = input("Podaj imię:\n")
    age = input("Podaj wiek:\n")

    print(f"Oto jest {name}, lat ma {age}!")


# Task 3
"""
    mkdir homework
    cd homework
    pwd
        .../Python/VS_Code/homework
    cd ..
"""


@task_separator
def task4():
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

    print(f"Pole prostokąta o wymiarach {side_a} x {side_b} wynosi {side_a*side_b}")


@task_separator
def task5():
    usd_val = 4.0
    question = f"Kurs USD wynosi {usd_val}. Ile zł chcesz przeznaczyć do wymiany?\n"
    while True:
        try:
            pln = input(question).strip()
            pln = float(pln.replace(",","."))
            break
        except ValueError:
            print("Podaj zapis wyłacznie w liczbach")
            continue
    print(f'Za {pln} zł uzyskasz {(pln/usd_val):.2f} dolarów')


@task_separator
def task6():
    while True:
        try:
            val = int(input("Podaj liczbę całkowitą\n"))
            break
        except ValueError:
            continue
    print(f"Zapis binarny: {bin(val)[2:]}")
    print(f"Zapis szesnastkowy: {hex(val)[2:]}")


@task_separator
def task7():
    word = input("Wpisz słowo:\n").casefold()
    back = word[::-1]
    print(f"{back.capitalize()} to palindrom.") if word == back else print(f"{word} od tyłu to {back}")


@task_separator
def task8():
    while True:
        try:
            val = int(input("Podaj liczbę całkowitą\n"))
            break
        except ValueError:
            continue
    print(f"{val} to liczba parzysta.") if val % 2== 0 else print(f"{val} to liczba nieparzysta")


@task_separator
def task9():
    while True:
        try:
            num1 = input("Podaj 1. liczbę\n")
            num1 = float(num1.replace(",","."))
            break
        except ValueError:
            continue
    while True:
        try:
            num2 = input("Podaj 2. liczbę\n")
            num2 = float(num2.replace(",","."))
            break
        except ValueError:
            continue
    while True:
        try:
            oper = input("Wpisz działanie do wykonania (-, +, /, *)\n")
            if oper in ("-","+", "/", "*"):
                break
        except:
            continue
    if oper == "-":
        res = num1 - num2
    elif oper == "+":
        res = num1 + num2
    elif oper == "/":
        if num2 == 0:
            print("Nie dzielimy przez 0! Wynik to nieskończoność.")
            return
        res = num1 / num2
        # uwzględnić brak dzielenia przez 0
    else:
        res = num1 * num2

    print(f"Wynik to {res}")
    

@task_separator
def task10():
    while True:
        try:
            adult = input('Z dorosłym jest? ["tak" / "nie"]\n')
            if adult.casefold() in ("tak","no","nie"):          
                break
        except ValueError:
            print("Normalnie mówi! Jak człowiek, a nie to!")
            continue

    while True:
        try:
            height = input("A ile ma centymetrów, że chce wejśc?\n")
            height = float(height.replace(",","."))
            break
        except ValueError:
            print("Nie wydziwia, tylko odpowiada!")
            continue

    if (height >= 120 and adult.casefold() in ("tak","no")) or height >= 160:
        print("No to wchodzi, kolejki nie blokuje.")
    elif height< 120:
        print("Za niski! Urośnie, to wróci. Następny!")
    else:
        print("Bez dorosłego nie wejdzie. Następny!")


if __name__ == "__main__":
    task1()
    task2()
    task4()
    task5()
    task6()
    task7()
    task8()
    task9()
    task10()
