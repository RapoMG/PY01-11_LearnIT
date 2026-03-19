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
    '''Analiza wieku: Napisz program, który pobiera od użytkownika wiek. Używając instrukcji
if-elif-else , wyświetl jeden z komunikatów: "Niemowlę" (0-1), "Dziecko" (2-12),
"Nastolatek" (13-17), "Dorosły" (18-64), "Senior" (65+).'''

    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    if 0 <= age <= 1:
        print("Infant")
    elif 2 <= age <= 12:
        print("Child")
    elif 13 <= age <= 17:
        print("Teenager")
    elif 18 <= age <= 64:
        print("Adult")
    elif age >= 65:
        print("Senior")
    else:
        print("Invalid age entered.")

@task_separator
def task2():
    '''Kalkulator zniżek: Napisz program, który oblicza cenę biletu. Cena bazowa to 100 PLN.
Jeśli użytkownik jest studentem ( tak/nie ) LUB ma mniej niż 18 lat, przysługuje mu 50%
zniżki. Użyj operatorów or i and .'''

    while True:
        try:
            age = int(input("Enter your age: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    is_student = input("Are you a student? (yes/no): ").strip().lower()

    base_price = 100
    discount = 0.5

    #if with unnecessary and or logic
    #if (age > 18 and is_student == "yes") or age < 18:

    if is_student == "yes" or age < 18:
        final_price = base_price * (1 - discount)
        print(f"You get a discount! The ticket price is: {final_price} PLN")
    else:
        print(f"The ticket price is: {base_price} PLN")

@task_separator
def task3():
    """Odliczanie do startu: Użyj pętli while , aby stworzyć program odliczający od 10 do 1. Po
odliczeniu, poza pętlą, program powinien wyświetlić "Start!"."""

    count = 10
    while count > 0:
        print(count)
        count -= 1
    print("Start!")


@task_separator
def task4():
    '''Literowanie słowa: Poproś użytkownika o podanie słowa. Użyj pętli for , aby wyświetlić
każdą literę tego słowa w osobnej linii, poprzedzoną jej indeksem. Przykład dla "Kot": 0:
K
, 1: o , 2: t .'''

    word = input("Enter a word: ")
    for index, letter in enumerate(word):
        print(f"{index}: {letter}")


@task_separator
def task5():
    '''Tabela mnożenia: Napisz program, który używając zagnieżdżonych pętli for (jedna w
drugiej), wyświetli tabliczkę mnożenia od 1 do 5. (Wskazówka: for i in range(1, 6):
for j in range(1, 6): ... ).'''

    for i in range(1, 6):
        for j in range(1, 6):
            print(f"{i} x {j} = {i * j}\n")
        


@task_separator
def task6():
    '''Gra "Zgadnij liczbę":
Program "myśli" o liczbie (np. sekret = 42 ).
Użyj pętli while True , aby w nieskończoność prosić użytkownika o podanie liczby.
Wewnątrz pętli, sprawdź, czy podana liczba jest równa sekretnej. Jeśli tak, wyświetl
gratulacje i użyj break , aby zakończyć grę. Jeśli nie, poinformuj, że to zła liczba.'''

    secret = 42
    while True:
        try:
            guess = int(input("Guess the number: "))
            if guess == secret:
                print("Congratulations! You've guessed the number!")
                break
            else:
                if guess < secret:
                    print("Too low, try again.")
                else:
                    print("Too high, try again.")
        except ValueError:
            print("Please enter a valid number.")


@task_separator
def task7():
    '''Tylko samogłoski: Poproś użytkownika o zdanie. Użyj pętli for oraz instrukcji continue ,
aby wyświetlić tylko samogłoski z tego zdania. (Wskazówka: if litera not in
"aeiouy": continue ).'''

    sentence = input("Enter a sentence:\n")
    vowels = "aeiouy"
    print("Vowels in the sentence:")
    for letter in sentence:
        if letter.lower() not in vowels:
            continue
        print(letter)


@task_separator
def task8():
    '''Wyszukiwarka w liście: Stwórz listę imion: imiona = ["Anna", "Jan", "Piotr",
"Kasia"] . Poproś użytkownika o podanie imienia do wyszukania. Użyj pętli for z
instrukcją break oraz blokiem else , aby:
    * Jeśli imię zostanie znalezione, wyświetlić "Znaleziono!" i przerwać pętlę.
    * Jeśli pętla zakończy się bez znalezienia imienia, wyświetlić "Nie znaleziono imienia na liście."
    '''

    names = ["Anna", "Jan", "Piotr", "Kasia"]
    search_name = input("Enter a name to search:\n").strip().title()

    for name in names:
        if name == search_name:
            print("Found!")
            break
    else:
        print("Name not found in the list.")


@task_separator
def task9():
    '''Potęgi dwójki: Użyj pętli while i skróconego operatora przypisania *= , aby wyświetlić
potęgi liczby 2, które są mniejsze niż 1000 (1, 2, 4, 8, ..., 512).'''

    power_of_two = 1
    while power_of_two < 1000:
        print(power_of_two)
        power_of_two *= 2
    

@task_separator
def task10():
    '''Prosty kalkulator walut:
    * Zdefiniuj kursy w słowniku, np. kursy = {"USD": 4.0, "EUR": 4.3} .
    * W pętli while True zapytaj użytkownika o kwotę w PLN i walutę (USD/EUR).
    * Użyj if-elif-else , aby sprawdzić wybraną walutę i obliczyć wynik.
    * Sformatuj wynik do dwóch miejsc po przecinku, używając f-stringa.
    * Zapytaj użytkownika, czy chce kontynuować. Jeśli odpowie "nie", użyj break .'''

    exchange_rates = {"USD": 4.0, "EUR": 4.3}
    while True:
        try:
            amount_pln = float(input("Enter the amount in PLN: "))
            currency = input("Enter the currency to convert to (USD/EUR): ").strip().upper()

            if currency in exchange_rates:
                converted_amount = amount_pln / exchange_rates[currency]
                print(f"{amount_pln:.2f} PLN is equal to {converted_amount:.2f} {currency}.")
            else:
                print("Unsupported currency. Please choose USD or EUR.")
                continue

            cont = input("Do you want to convert another amount? (yes/no): ").strip().lower()
            if cont == "no":
                break
        except ValueError:
            print("Please enter a valid number for the amount.")





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
