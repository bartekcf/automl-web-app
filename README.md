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

Do uruchomienia projektu wymagane są:

- Docker,
- Docker Compose.

Nie jest wymagane ręczne instalowanie Pythona ani bibliotek.

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
api/         - backend FastAPI
frontend/    - interfejs Streamlit
models/      - zapisany model uczenia maszynowego
data/        - baza danych
notebooks/   - notebook wykorzystany podczas pracy nad modelem
```
