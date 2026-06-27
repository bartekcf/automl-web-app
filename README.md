# Used Car Price Predictor

Aplikacja internetowa służąca do przewidywania ceny używanego samochodu na podstawie podanych parametrów pojazdu.

## Autorzy

- Paweł Lipiec s27644
- Bartłomiej Kędziora s27612


## Funkcjonalność

Aplikacja pozwala:

- wybrać markę i model samochodu,
- podać podstawowe dane pojazdu,
- określić parametry silnika i wyposażenia,
- uzyskać przewidywaną cenę samochodu.

Interfejs użytkownika został wykonany w Streamlit, natomiast backend aplikacji działa w FastAPI.

## Wymagania

Wymagania środowiskowe

Do uruchomienia projektu wymagane są:

Docker,
Docker Compose,
przeglądarka internetowa.

Projekt można uruchomić na systemie Windows, macOS lub Linux.

W przypadku Windows i macOS należy zainstalować Docker Desktop. Nie jest wymagane ręczne instalowanie Pythona ani bibliotek, ponieważ wszystkie zależności są instalowane automatycznie w kontenerach.

## Uruchomienie aplikacji

Należy rozpakować otrzymane archiwum ZIP, a następnie przejść w terminalu do katalogu głównego projektu.

W katalogu zawierającym plik `docker-compose.yml` należy uruchomić:


```bash
docker compose up --build
```

Po uruchomieniu aplikacja będzie dostępna pod adresem:

```text
http://localhost:8501
```

Dokumentacja FastAPI jest dostępna pod adresem:

```text
http://localhost:8000/docs
```

Aby zatrzymać aplikację, należy użyć polecenia:

```bash
docker compose down
```

## Sposób użycia

Po otwarciu aplikacji należy:

1. wybrać markę i model samochodu,
2. uzupełnić pozostałe dane pojazdu,
3. nacisnąć przycisk odpowiedzialny za wykonanie predykcji,
4. odczytać przewidywaną cenę.

## Wymagane pliki

Projekt korzysta z gotowego modelu uczenia maszynowego oraz bazy danych zawierającej wartości wykorzystywane w formularzu.

Wymagane pliki znajdują się w katalogach:

```text
models/
data/
```

Pliki te są już częścią projektu i nie wymagają dodatkowego pobierania.

## Struktura projektu

```text
.
├── README.md                         # Dokumentacja projektu oraz instrukcja jego uruchomienia
│
├── api/                              # Backend aplikacji oparty na FastAPI
│   ├── Dockerfile                    # Buduje obraz API, instaluje zależności przez uv
│   │                                 # i uruchamia serwer Uvicorn na porcie 8000
│   ├── main.py                       # Główna aplikacja FastAPI; ładuje model ML,
│   │                                 # pobiera dane z SQLite i udostępnia endpointy:
│   │                                 # /options, /models oraz /predict
│   ├── pyproject.toml                # Konfiguracja projektu API i jego zależności Python
│   └── uv.lock                       # Zablokowane wersje zależności API używane przez uv
│
├── data/                             # Dane wykorzystywane przez aplikację
│   └── db.sqlite                     # Baza SQLite zawierająca dane o samochodach,
│                                     # używane m.in. do wypełniania list wyboru
│
├── docker-compose.yml                # Konfiguracja kontenerów API i frontendu;
│                                     # udostępnia porty 8000 i 8501 oraz montuje
│                                     # katalogi models i data w kontenerze API
│
├── frontend/                         # Interfejs użytkownika oparty na Streamlit
│   ├── Dockerfile                    # Buduje obraz frontendu i uruchamia aplikację Streamlit
│   ├── pyproject.toml                # Konfiguracja frontendu i zależności:
│   │                                 # Streamlit oraz Requests
│   ├── streamlit_app.py              # Formularz do wprowadzania parametrów samochodu;
│   │                                 # pobiera opcje z API, wysyła żądanie predykcji
│   │                                 # i wyświetla przewidywaną cenę pojazdu
│   └── uv.lock                       # Zablokowane wersje zależności frontendu
│
├── main.py                           # Domyślny plik utworzony dla głównego projektu Python;
│                                     # nie jest wykorzystywany przez kontenery aplikacji
│
├── models/                           # Wytrenowane i zapisane modele uczenia maszynowego
│   └── used_car_price_model.pkl      # Pakiet zawierający wytrenowany pipeline,
│                                     # listę cech modelu oraz dane potrzebne do predykcji
│
├── notebooks/                        # Notebooki używane podczas tworzenia modelu
│   └── EDA_used_car_price.ipynb      # Eksploracyjna analiza danych, przygotowanie danych,
│                                     # trenowanie i ocena modeli oraz zapis modelu końcowego
│
├── pyproject.toml                    # Główna konfiguracja środowiska Python projektu,
│                                     # używanego m.in. podczas pracy z notebookiem
└── uv.lock                           # Zablokowane wersje głównych zależności projektu
```
