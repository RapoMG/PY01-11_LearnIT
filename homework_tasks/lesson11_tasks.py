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
    """Inicjalizacja repozytorium i pierwszy commit
    1.Zainicjalizuj nowe repozytorium Git w dowolnym katalogu na swoim komputerze.
2. Stwórz plik README.md i dodaj do niego krótki opis projektu.
3. Dodaj plik do obszaru staging i zatwierdź zmiany z odpowiednim komunikatem
commit.
4. Wyświetl historię commitów za pomocą git log .
Oczekiwany rezultat: Wykonanie poleceń git init, git add, git commit i git log poprawnie
wyświetli historię commitów."""

    #Set default editor to nano
    #git config --global core.editor "nano"

    print("""
    GIT BASH COMMANDS:
        $ mkdir new_repo
        $ cd new_repo
        $ git init
            Initialized empty Git repository in /Python/VS_Code/homework/new_repo/.git/
        
        $ nano README.md
            This is repo for lesson 11 home tasks.
        
        $ git add README.md
          warning: in the working copy of 'README.md', LF will be replaced by CRLF the next time Git touches it

        $ git commit -m "initiating repo"
            [master (root-commit) 6448f70] initiating repo
            1 file changed, 1 insertion(+)
            create mode 100644 README.md

        $ git log .
            commit 6448f70e3e039b8761d5f7ae251af9da738d3ed7 (HEAD -> master)
            Author: RapoMG <rapomg@gmail.com>
            Date:   Sat Jan 17 20:28:34 2026 +0100

                initiating repo

    """)



@task_separator()
def task2():
    """Praca z gałęziami
    1. Utwórz nową gałąź o nazwie feature-login .
    2. Przełącz się na nową gałąź i dodaj nowy plik login.py (lub login.html jeśli wolisz).
    3. Zatwierdź zmiany w tej gałęzi i przełącz się z powrotem na main .
    4. Spróbuj połączyć gałąź feature-login z main i rozwiąż ewentualne konflikty
    Oczekiwany rezultat: Powstanie nowej gałęzi, zatwierdzenie zmian, scalanie bez błędów lub
    rozwiązanie konfliktów."""

    print("""
        GIT BASH COMMANDS:
            $ git branch feature-login
            $ git checkout feature-login
                Switched to branch 'feature-login'

            $ nano login.py
                pass
            $ git add .
                warning: in the working copy of 'login.py', LF will be replaced by CRLF the next time Git touches it
            
            $ git commit -m "adds empty login.py file"
                [feature-login b475c33] adds empty login.py file
                1 file changed, 1 insertion(+)
                create mode 100644 login.py

            $ git checkout master
                Switched to branch 'master'

            $ git merge feature-login
                [master 065c83b] Merge branch 'feature-login'
          """)


@task_separator()
def task3():
    """Klonowanie i współpraca

1. Sklonuj podane na zajęciach repozytorium z GitHub (lub stwórz własne puste
repozytorium na GitHub i sklonuj je).
2. Dodaj nowy plik contributors.txt , wpisz w nim swoje imię i nazwisko.
3. Stwórz nową gałąź, zatwierdź zmiany i wypchnij je do zdalnego repozytorium.
4. Utwórz Pull Request (lub Merge Request) na platformie GitHub/GitLab/Bitbucket i
opisz zmiany.
Oczekiwany rezultat: Klonowanie repozytorium, dodanie pliku, utworzenie PR/MR."""

    print("""
        GIT BASH COMMANDS:

            $ git clone https://github.com/RapoMG/PY01-11_LearnIT
                Cloning into 'PY01-11_LearnIT'...
                remote: Enumerating objects: 3, done.
                remote: Counting objects: 100% (3/3), done.
                remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
                Receiving objects: 100% (3/3), done.
          
            $ cd PY01-11_LearnIT
          
            $ git checkout -b test_branch
                Switched to a new branch 'test_branch'

            $ nano contributors.txt
                Krzysztof
          
            $ git add contributors.txt
                warning: in the working copy of 'contributors.txt', LF will be replaced by CRLF the next time Git touches it

            $ git commit -m "Add contributor: Krzysztof"
                [test_branch (root-commit) 37e61a7] Add contributor: Krzysztof
                1 file changed, 1 insertion(+)
                create mode 100644 contributors.txt

            $ git push origin test_branch
                Enumerating objects: 4, done.
                Counting objects: 100% (4/4), done.
                Delta compression using up to 6 threads
                Compressing objects: 100% (2/2), done.
                Writing objects: 100% (3/3), 294 bytes | 294.00 KiB/s, done.
                Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
                remote:
                remote: Create a pull request for 'test_branch' on GitHub by visiting:
                remote:      https://github.com/RapoMG/PY01-11_LearnIT/pull/new/test_branch
                remote:
                To https://github.com/RapoMG/PY01-11_LearnIT
                * [new branch]      test_branch -> test_branch

        VIA BROWSER
            > go to https://github.com/RapoMG/PY01-11_LearnIT
            > press [Compare & pull request]
            > Add a description:
                Adding a contributors.txt file with my name
            > press [Create Pull Request]
          """)

    
@task_separator()
def task4():
    """Konfiguracja projektu
1. Utwórz nową repozytorię:
mkdir team-project-basic
cd team-project-basic
git init
2. Skonfiguruj swoje dane użytkownika dla tej repozytorium:
git config user.name "Twoje Imię"
git config user.email "twoj.email@example.com"
"""

    print("""
        GIT BASH COMMANDS:
            $ mkdir team-project-basic

            $ cd team-project-basic

            $ git init
                Initialized empty Git repository in K:/Przestrzeń robocza/Python/VS_Code/homework/team-project-basic/.git/

            $ git config user.name "Krzysztof"
          
            $ git config user.mail "k.janiak.82@gmail.com"
          """)
   

@task_separator()
def task5():
    """Praca z plikami i commitami
1. W repozytorium team-project-basic (z Zadania 4) stwórz plik app.py z prostym
kodem Pythona (np. funkcja hello_world ).
2. Dodaj app.py do obszaru staging.
3. Wykonaj commit z komunikatem zgodnym z Conventional Commits (np. feat: add
hello world function ).
4. Zmodyfikuj app.py (np. zmień komunikat funkcji).
5. Sprawdź status repozytorium ( git status ).
6. Dodaj zmieniony plik do stagingu i wykonaj kolejny commit (np. fix: update hello world
message)."""

    print("""
        GIT BASH COMMANDS:
            $ nano app.py 
                print("Hello word!\n Again!")

            $ git add app.py
                warning: in the working copy of 'app.py', LF will be replaced by CRLF the next time Git touches it

            $ $ git commit -m "feat: prints hello word."
                [master (root-commit) 03fc50e] feat: prints hello word.
                1 file changed, 2 insertions(+)
                create mode 100644 app.py

            $ nano app.py 
                print("Oh, no! Goodbye word!")
            
            $ git status
                On branch master
                Changes not staged for commit:
                (use "git add <file>..." to update what will be committed)
                (use "git restore <file>..." to discard changes in working directory)
                        modified:   app.py
                no changes added to commit (use "git add" and/or "git commit -a")

            $ git add app.py
                warning: in the working copy of 'app.py', LF will be replaced by CRLF the next time Git touches it

            $ git commit -m "fix(print): one useless message changed to another one"
                [master 1cc4f26] fix(print): one useless message changed to another one
                1 file changed, 1 insertion(+), 1 deletion(-)

          """)

@task_separator()
def task6():
    """Resetowanie i przywracanie zmian
1. Wprowadź kilka zmian w istniejącym pliku i dodaj je do stagingu ( git add ).
2. Wycofaj te zmiany z obszaru staging ( git reset HEAD <plik> ).
3. Wprowadź kolejne zmiany w tym samym pliku i wykonaj commit.
4. Cofnij się do commita sprzed tych ostatnich zmian za pomocą git reset --hard
<hash_commita> . Upewnij się, że rozumiesz, co robi --hard.
Oczekiwany rezultat: Zmiany poprawnie cofnięte lub przywrócone do wcześniejszego stanu.
"""
    print("""
        GIT BASH COMMANDS:
            $ nano app.py 
                defdef hello_word():
                    return "Now I'm serious function!"

                print(hello_word())
          
            $ git add app.py
                warning: in the working copy of 'app.py', LF will be replaced by CRLF the next time Git touches it

            $ git reset HEAD app.py
                Unstaged changes after reset:
                M       app.py

            $ nano app.py
                def hello_word(test: str):
                    return f"I print {test}."

                print(hello_word("word"))
          

            $ git add app.py
                warning: in the working copy of 'app.py', LF will be replaced by CRLF the next time Git touches it

            $ git commit -m "feat: Changed to function, prints string that was send there"
                [master 15bb9a6] feat: Changed to function, prints string that was send there
                1 file changed, 4 insertions(+), 1 deletion(-)

            $ git log
                commit 15bb9a69126b23c9d90ed712324d4f14949c8a3d (HEAD -> master)
                Author: Krzysztof <k.janiak.82@gmail.com>
                Date:   Sun Jan 18 22:25:45 2026 +0100

                    feat: Changed to function, prints string that was send there

                commit 1cc4f26476eb73ef1aeb77cda4b5a2401d3c1c38
                Author: Krzysztof <k.janiak.82@gmail.com>
                Date:   Sun Jan 18 21:41:34 2026 +0100

                    fix(print): one useless message changed to another one

                commit 03fc50e7ba1a201451e3dbbda0de35a756faecd5
                Author: Krzysztof <k.janiak.82@gmail.com>
                Date:   Sun Jan 18 21:33:56 2026 +0100

                    feat: prints hello word.
             
            $ git reset --hard 1cc4f26476eb73ef1aeb77cda4b5a2401d3c1c38
                HEAD is now at 1cc4f26 fix(print): one useless message changed to another one

          """)
    

@task_separator()
def task7():
    """Rebase i interaktywna edycja historii

1. Utwórz nową gałąź feature-branch z main .
2. W gałęzi feature-branch wykonaj trzy oddzielne commity, każdy z małą, prostą
zmianą (np. dodaj jedną linię do pliku, zmień drugą, dodaj komentarz).
3. Użyj git rebase -i HEAD~3 , aby połączyć te trzy commity w jeden spójny commit.
Zmień typ commita na feat i użyj konwencji Conventional Commits.
4. Wypchnij zmiany do zdalnego repozytorium (jeśli wymagane, użyj git push --force
– pamiętaj, że to nadpisuje historię!).
Oczekiwany rezultat: Historia commitów została poprawnie zmieniona i wypchnięta.
"""
    
    print("""
        GIT BASH COMMANDS:
            $ git checkout -b feature-branch
                Switched to a new branch 'feature-branch'
          
            $ nano app.py

            $ git add app.py
                from random import randit
                print("Oh, no!\n Goodbye word!")
                def die():
                    return randit(1, 100)

            $ git commit -m "feat: added dice roll function"
                [feature-branch b74431e] feat: added dice roll function
                1 file changed, 3 insertions(+), 1 deletion(-)

            $ nano app.py

            $ git add app.py
                from random import randit
                
                def die():
                    return randit(1, 100)
          
            $ git commit -m "fix: removed redundant print"
                [feature-branch 70d79bb] fix: removed redundant print
                1 file changed, 1 insertion(+), 1 deletion(-)

            $ nano app.py

            $ git add app.py
                from random import randit

                def die():
                   '''return: random int in range 1-100'''
                    return randit(1, 100)
          
            $ git commit -m "style: added function docstring"
                [feature-branch 49fd91e] style: added function docstring
                1 file changed, 1 insertion(+)

            $ git rebase -i HEAD~3

            IN THE EDITOR:
                pick b74431e feat: added dice roll function
                pick 70d79bb fix: removed redundant print
                pick 49fd91e style: added function docstring

            CHANGED TO:
                pick b74431e feat: added dice roll function
                squash 70d79bb fix: removed redundant print
                squash 49fd91e style: added function docstring
          
            COMMMENT EDITION:
                fix(print): one useless message changed to another one
          
            [detached HEAD 5b785b1] feat(die): added dice roll function with documentation
            Date: Sun Jan 18 23:57:31 2026 +0100
            1 file changed, 4 insertions(+), 1 deletion(-)
            Successfully rebased and updated refs/heads/feature-branch.
        
            $ git push origin feature-branch
                fatal: 'origin' does not appear to be a git repository
                fatal: Could not read from remote repository.

                Please make sure you have the correct access rights
                and the repository exists.
          
            TROUBLESHOOTING:
          
            $ git remote -v

            $ git remote add origin https://github.com/RapoMG/PY01-11_LearnIT.git

            $ git remote -v
                origin  https://github.com/RapoMG/PY01-11_LearnIT.git (fetch)
                origin  https://github.com/RapoMG/PY01-11_LearnIT.git (push)


            $ git push origin feature-branch
                Enumerating objects: 9, done.
                Counting objects: 100% (9/9), done.
                Delta compression using up to 6 threads
                Compressing objects: 100% (4/4), done.
                Writing objects: 100% (9/9), 846 bytes | 846.00 KiB/s, done.
                Total 9 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
                remote:
                remote: Create a pull request for 'feature-branch' on GitHub by visiting:
                remote:      https://github.com/RapoMG/PY01-11_LearnIT/pull/new/feature-branch
                remote:
                To https://github.com/RapoMG/PY01-11_LearnIT.git
                * [new branch]      feature-branch -> feature-branch

          """)


@task_separator()
def task8():
    """Rozwiązywanie konfliktów w Git
1. Utwórz repozytorium lokalnie i zainicjalizuj Git ( git init ).
2. Dodaj plik conflict_example.txt , wpisz do niego pierwszą linię tekstu (np. Linia
1 - wersja glowna ) i wykonaj commit ( git commit -m "feat: dodano pierwsza
linie" ).
3. Utwórz nową gałąź branch-A ( git checkout -b branch-A ) i edytuj
conflict_example.txt , dodając drugą linię (np. Linia 2 - z branch-A ).
Zatwierdź zmiany ( git commit -m "feat: dodano druga linie w branch-A" ).
4. Przełącz się na main ( git checkout main ) i również edytuj
conflict_example.txt , ale w inny sposób (np. zmień pierwszą linię na Linia 1 -
zmieniona w main i dodaj nową linię Linia 2 - z main ). Zatwierdź zmiany ( git
commit -m "fix: zmieniono pierwsza linie i dodano druga w main" ).
5. Spróbuj scalić branch-A z main ( git merge branch-A ). Zauważysz konflikt.
6. Rozwiąż powstały konflikt w pliku conflict_example.txt , edytując go ręcznie, a
następnie dodaj rozwiązany plik do stagingu ( git add conflict_example.txt ).
7. Zatwierdź poprawioną wersję pliku i zakończ scalanie ( git commit ).
Oczekiwany rezultat: Poprawnie rozwiązany konflikt merge w pliku conflict_example.txt.
(challenge)"""
    
    print("""
        $ mkdir next_test

        $ cd next_test

        $ git init
            Initialized empty Git repository in Python/VS_Code/homework/next_test/.git/

        $ nano conflict_example.txt
            Linia 1 - wersja główna
        
        $ git add conflict_example.txt
            warning: in the working copy of 'conflict_example.txt', LF will be replaced by CRLF the next time Git touches it
        
        $ git commit -m "feat: dodano pierwszą linię"
            [master (root-commit) cf85ec1] feat: dodano pierwszą linię
            1 file changed, 1 insertion(+)
            create mode 100644 conflict_example.txt
          
        $ git checkout -b branch-A
            Switched to a new branch 'branch-A'

        $ nano conflict_example.txt

        $ git add conflict_example.txt
            warning: in the working copy of 'conflict_example.txt', LF will be replaced by CRLF the next time Git touches it

        $ git commit -m "feat: dodano drugą linię w branch-A"
            [branch-A 1df2fdc] feat: dodano drugą linię w branch-A
            1 file changed, 1 insertion(+)

        $ git checkout master
            Switched to branch 'master'


        $ nano conflict_example.txt

        $ git add conflict_example.txt

        $ git commit -m "fix: zmieniono 1 linie dodano drugą w main"
            [master feac527] fix: zmieniono 1 linie dodano drugą w main
            1 file changed, 2 insertions(+), 1 deletion(-)

        $ git merge branch-A
            Auto-merging conflict_example.txt
            CONFLICT (content): Merge conflict in conflict_example.txt
            Automatic merge failed; fix conflicts and then commit the result.

        $ nano conflict_example.txt
            <<<<<<< HEAD
            Linia 1 - zmieniona w main
            Linia 2 - dodana w main
            =======
            Linia 1 - wersja główna
            Linia 2 - z branch-A
            >>>>>>> branch-A
        
        EDITED TO:
            Linia 1 - zmieniona w main
            Linia 2 - z branch-A
          
        $ git add conflict_example.txt


        $ git commit
            [master 59b858a] Merge branch 'branch-A'

          """)

@task_separator()
def task9():
    """Zastosowanie Conventional Commits 
W ramach dowolnego z poprzednich zadań, upewnij się, że wszystkie Twoje commity są
zgodne z konwencją Conventional Commits. Stosuj typy takie jak feat, fix, docs, style i
dodawaj zakres, jeśli to ma sens. Dodatkowo, użyj opcjonalnego body (szczegółowego
opisu) dla co najmniej jednego commita, wyjaśniając, dlaczego zmiana została
wprowadzona."""

    print("""
        $ git log --oneline
            59b858a (HEAD -> master) Merge branch 'branch-A'
            feac527 fix: zmieniono 1 linie dodano drugą w main
            1df2fdc (branch-A) feat: dodano drugą linię w branch-A
            cf85ec1 feat: dodano pierwszą linię
          
        $ git commit --amend
            Merge branch 'branch-A'

            Merge conflict resolution:
            kept Line 1 changed in main
            kept Line 2 changed in branch-A

        
            [master 7fa9818] Merge branch 'branch-A'
            Date: Mon Jan 19 14:30:22 2026 +0100


        """)

@task_separator(True)
def task10():
    """Praca z Git Flow (zaawansowane)
Jeśli masz zainstalowane narzędzie git-flow (lub jesteś gotów symulować jego działanie
ręcznymi komendami git branch/git checkout/git merge):

1. Zainicjalizuj git flow w nowym repozytorium.
2. Rozpocznij nową funkcjonalność ( git flow feature start moja-funkcja ).
3. Wprowadź kilka commitów na tej gałęzi.
4. Zakończ funkcjonalność ( git flow feature finish moja-funkcja ).
5. Zauważ, jak zmiany zostały scalone z gałęzią develop .
6. Następnie, rozpocznij gałąź wydania ( git flow release start 1.0.0 ).
7. Wprowadź "poprawkę" w gałęzi wydania (np. zmień coś w pliku i zatwierdź).
8. Zakończ wydanie ( git flow release finish 1.0.0 ). Zauważ, jak wydanie zostało
scalone zarówno z main , jak i develop , a poprawka jest widoczna w obu gałęziach. 
Oczekiwany rezultat: Zrozumienie i praktyczne zastosowanie cyklu życia gałęzi w Git Flow.
(challenge)"""


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
    # task10()
 