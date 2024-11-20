## Uruchamianie programu po raz pierwszy

Aby móc uruchomić test należy:
* pobrać i zainstalować IDE np. VSC
* zainstalować pythona
* w terminalu IDE zainstalować playwright oraz pytest


## Uruchomienie testu:

* w terminalu wybrać ścieżkę do projektu /ścieżka/do/folderu/tests/lub/pojedynczego/testu
* po ścieżce dodać **py -m pytest test_change_cookie.py** - uruchamia sam test w tle, w terminalu widoczny wynik passed / failed
$ py -m pytest test_change_cookie.py --headed - uruchamia test w widoczną akcją na przeglądarce
$ py -m pytest --html=report.html --self-contained-html test_change_cookie.py - generuje raport w postaci html
$ py -m pytest --junitxml=report.xml  --html=report.html --self-contained-html test_change_cookie.py - dodatkowo wtorzy raport w junitxml


## Uruchamianie testu równocześnie na 3 przeglądarkach:

* doinstalować paczkę **py -m pip install pytest-xdist**
$ py -m pytest test_change_cookie.py --browser chromium --browser firefox --browser webkit -n auto
 flaga n-auto uruchamia testy równolegle, co pozwala skrócić czas wykonywania o połowę w stosunku do uruchamianych testów bez tej flagi

$ py -m pytest --html=report.html --self-contained-html --browser chromium --browser firefox --browser webkit -n auto
