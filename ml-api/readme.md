# Przewidywanie Wypisów Studentów - REST API i Airflow

Ten projekt ustawia **środowisko Airflow**, które przetwarza dane, trenuje model uczenia maszynowego, a także udostępnia **serwis REST API** do przewidywania wypisów i sukcesów akademickich studentów. API udostępnia prosty interfejs do interakcji z wytrenowanym modelem.

## Spis Treści
- [Rozpoczęcie pracy](#rozpoczęcie-pracy)
- [Ustawienie Airflow](#ustawienie-airflow)
- [Ustawienie REST API](#ustawienie-rest-api)
- [Testowanie API](#testowanie-api)
  - [Za pomocą `curl`](#za-pomocą-curl)
  - [Za pomocą Postman](#za-pomocą-postman)

## Rozpoczęcie pracy

Aby rozpocząć, upewnij się, że masz zainstalowane **Docker** oraz **Docker Compose** na swoim komputerze.

### Wymagania
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Uruchomienie środowiska za pomocą Docker Compose
Aby uruchomić zarówno **Airflow**, jak i **REST API**, uruchom poniższe polecenie:
```bash
docker-compose up --build
```
To polecenie:
- Zbuduje kontenery (Airflow, ML API).
- Uruchomi kontenery, w tym Airflow z wszystkimi DAG-ami oraz REST API.

**Uwaga**: To polecenie wystawi:
- Interfejs Web UI Airflow na `http://localhost:8080`
- Serwis REST API na `http://localhost:5000`

---

### Endpointy API

- **POST /predict** – Endpoint do wysyłania danych wejściowych i uzyskiwania prognoz.

---

## Testowanie API

### Przykładowe dane testowe

Do przetestowania api został przygotowany plik `example_data.json`, który znajduje się w tym repozytorium.

### Za pomocą `curl`

Możesz przetestować API za pomocą narzędzia `curl` w terminalu. Oto przykład wysłania żądania POST do endpointu `/predict`:

```bash
curl -X POST http://localhost:5000/predict \
    -H "Content-Type: application/json" \
    -d '{dane w formacie pliku example_data.json}'
```

W powyższym przykładzie:
- `-X POST` określa metodę HTTP.
- `-H "Content-Type: application/json"` ustawia nagłówek, że dane wejściowe będą w formacie JSON.
- `-d` wysyła dane wejściowe w formacie JSON, które będą analizowane przez model.

### Za pomocą Postman

1. Otwórz Postman.
2. Utwórz nowe żądanie `POST`.
3. Wprowadź URL: `http://localhost:5000/predict`.
4. Ustaw nagłówek `Content-Type` na `application/json`.
5. Wprowadź dane wejściowe w formacie JSON w sekcji body, np.:
   ```json
   {
     dane w formacie pliku example_data.json
   }
   ```
6. Kliknij "Send", aby wysłać żądanie i uzyskać odpowiedź z prognozami.

---

## Podsumowanie

W tym projekcie skonfigurowano środowisko Airflow do przetwarzania danych oraz serwis REST API, który umożliwia interakcję z wytrenowanym modelem. Po uruchomieniu środowiska za pomocą Docker Compose, możesz łatwo testować API, wysyłając żądania POST z danymi wejściowymi.