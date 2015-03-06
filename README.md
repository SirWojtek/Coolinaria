## Coolinaria

### Wymagania
- obsluga uzytkowników:
   - administrator,
   - moderator,
   - uzytkownik
- mozliwosc przegladania osób niezalogowanych,
- statystyki,
- serwowanie przepisów,
- dodawanie przepisów,
- wyszukiwanie po skladniku,
- przepisy maja zdefiniowane skladniki,
- podzial przepisów (sniadanie, obiad, kolacja)
- wyswietlanie popularnych skladników (kafelki),
- zarzadzanie uzytkownikiem
    - zmiana hasla,
    - ile dodal przepisow,

### Schemat bazy danych

##### Przepis
- array Skladnik przepisu,
- array Rodzaj,
- string Wykonanie,
- Obrazek obraz,
- Uzytkownik ktoDodal,
- Data dataDodania

##### Skladnik przepisu
- Skladnik skladnik,
- string ilosc

##### Skladnik
- string nazwa,
- string opis,
- bool moznaWyszukiwac (soli nie mozna),
- Obrazek obraz

##### Uzytkownik
- string Login (e-mail),
- string haslo,
- array Przepis,

### Technologia
- frontend: AngularJS
- backend: python + RestAPI + JSON
- baza daych: ??
- dokumentacja: Doxygen
- repo: GitHub
- system: Linux na wirtualce PWr (Ubuntu)
- projekt: Redmine
- grupa dyskusyjna

### Wstepny podzial zadan:
- frontend: Marcin, Mazi
- backend: Hubert, Mateusz, Szymon
- dokumentacja: kazdy swoja czesc, Szymon nadzoruje
- Doxygen: Hubert
- repo: Mateusz
- wirtualka: Mateusz
- dokument dla Nikodema - Szymon

### Taski
- Serwer na wirtualce - Mateusz
- Redmine - Mazi
- Toolchain (python + django + AngularJS + baza danych) - Hubert
- Deoxygen - Hubert
- Import przepisów do bazy danych (http://api.bigoven.com/) - Szymon
- grupa dyskusyjna - Marcin

### Milestone
1. Przygotowane srodowisko (17.03.2015)
    - skonfigurowana baza danych,
    - przygotowane narzedzia programistyczne i deweloperskie,
      - Linux (wirtualka),
      - Redmine,
      - GitHub,
      - Deoxygen,
      - python + Django,
      - baza danych,
      - grupa dyskusyjna,
    - dzialajacy serwer Webowy,
    - lacznosc z maszyna wirtualna,
    - HelloWorld
2. Kompletna specyfikacja projektu (31.03.2015)
   - widoki,
   - schemat bazy danych,
   - architektura aplikacji,
   - definicje interfejsow,
   - definicja funkcjonalnosci,
   - user stories (przypadki uzycia),
   - dokumentacja,
3. Implementacja podstawowych funkcjonalnosci (sprint 1) (21.04.2015)
    - podstawowe widoki aplikacji,
    - obsluga uzytkownika (wraz z poziomami uzytkowników),
    - panel administracyjny,
    - przykladowe przepisy i skladniki w bazie danych,
    - dokuentacja techniczna pracy,
4. Implemenctacja funkcjonalnosci kluczowych (sprint 2) (12.05.2015)
    - wyszukiwanie przepisow po skladniku,
    - dodawanie i usuwanie przepisow,
    - widoki do powyzszych funkcjonalnosci,
    - kompletna baza przepisów i skladników,
    - testowanie i poprawa bledów,
    - dokuentacja techniczna pracy
5 Finalna wersja aplikacji (sprint 3) (1.06.2015)
    - implementacja statystyk uzytkowania,
    - dokumentacja uzytkownika,
    - aplikacja zgodna z wymaganiami,
    - testy funkcjonalne aplikacji,
    - przygotowanie projektu do instalacji i wdrozenia

###Uwagi
- kazdy uzupelnia instrukcje instalacji (by Szymon),
- dokumentacja TYLKO po polsku,
