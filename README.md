# Predykcja ryzyka rezygnacji ze studiów i sukcesu akademickiego studentów

---

## 1. Opis tematu i problemu biznesowego/technicznego

**Temat:**  
Celem projektu jest zbudowanie modelu predykcyjnego oceniającego ryzyko rezygnacji ze studiów oraz sukcesu akademickiego studentów na podstawie dostępnych danych. Wczesne zidentyfikowanie studentów zagrożonych rezygnacją z nauki lub słabymi wynikami akademickimi może pomóc uczelniom w opracowaniu lepszych strategii wsparcia i interwencji, co wpłynie pozytywnie na retencję i sukces studentów.

**Problem do rozwiązania:**  
Rezygnacja ze studiów stanowi istotny problem dla uczelni i studentów, wpływając zarówno na wskaźniki ukończenia programów, jak i na reputację uczelni. Jednocześnie sukces akademicki studentów jest kluczowy dla ich przyszłych możliwości zawodowych. Celem projektu jest zbudowanie modelu, który pomoże identyfikować studentów w grupie ryzyka, aby można było wdrożyć odpowiednie działania wspierające, takie jak doradztwo akademickie, mentoring lub programy wsparcia finansowego.

---

## 2. Źródło danych, charakterystyka i uzasadnienie wyboru

**Źródło danych:**  
Dane pochodzą z [Predict Students Dropout and Academic Success Dataset](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success) dostępnego w UCI Machine Learning Repository.

**Charakterystyka danych:**  
Zbiór danych zawiera informacje dotyczące studentów uczelni wyższej, obejmujące m.in.:
   - **Cechy demograficzne i społeczno-ekonomiczne**: wiek, płeć, status ekonomiczny.
   - **Cechy akademickie**: średnia ocen, liczba nieobecności, poziom edukacji rodziców.
   - **Dane o uczestnictwie i zaangażowaniu**: udział w zajęciach, frekwencja, aktywność w kursach.

**Uzasadnienie wyboru:**  
Zbiór danych zawiera różnorodne zmienne dotyczące studentów, które mogą mieć wpływ na ryzyko rezygnacji ze studiów oraz osiągnięcia akademickie. Zbiór danych pozwala na eksplorację czynników, które są istotne dla sukcesu akademickiego, co umożliwia zbudowanie modelu opartego na rzeczywistych danych, który może pomóc uczelniom w efektywnym wsparciu swoich studentów.

---

## 3. Cele projektu

**Główne cele projektu:**  
1. **Analiza danych** – Przeprowadzenie wstępnej analizy danych, identyfikacja brakujących wartości oraz analiza rozkładów zmiennych.
2. **Eksploracja zależności między zmiennymi** – Zidentyfikowanie kluczowych cech, które wpływają na ryzyko rezygnacji ze studiów i sukces akademicki.
3. **Budowa i trenowanie modelu predykcyjnego** – Zastosowanie modeli klasyfikacyjnych (np. lasów losowych, regresji logistycznej, sieci neuronowych) do przewidywania, czy student ukończy studia z sukcesem czy zrezygnuje.
4. **Walidacja i ocena modelu** – Ocena skuteczności modelu za pomocą miar takich jak precyzja, czułość, F1-score oraz ROC-AUC.
5. **Przygotowanie modelu do wdrożenia** – Optymalizacja i przygotowanie modelu do wdrożenia, aby mógł wspierać działania uczelni.
6. **Dokumentacja i raport końcowy** – Przygotowanie dokumentacji i raportu końcowego wraz z prezentacją wyników.

---

## 4. Ogólna struktura pracy nad modelem

**Struktura pracy:**  
Praca nad modelem zostanie podzielona na następujące etapy:

1. **Pobranie i przygotowanie danych**
   - Pobranie danych ze źródła.
   - Przeprowadzenie wstępnej analizy danych (EDA) i czyszczenie danych, w tym uzupełnienie lub usunięcie brakujących wartości.
   - Podział danych na zbiór treningowy (70%) i testowy (30%).

2. **Analiza i eksploracja danych**
   - Analiza rozkładów atrybutów i wizualizacja zależności między zmiennymi.
   - Identyfikacja istotnych cech, takich jak obecność nieobecności, średnia ocen i status społeczno-ekonomiczny.

3. **Trenowanie modelu**
   - Wybór modeli klasyfikacyjnych (np. las losowy, regresja logistyczna, drzewa decyzyjne).
   - Optymalizacja hiperparametrów dla wybranych modeli.
   - Wytrenowanie modeli na zbiorze treningowym.

4. **Walidacja i testowanie modelu**
   - Ocena jakości modelu na zbiorze testowym.
   - Użycie miar takich jak precyzja, czułość, F1-score i ROC-AUC w celu oceny jakości modelu.

5. **Dokształcanie modelu** (jeśli zajdzie potrzeba)
   - Dalsze trenowanie na nowych danych lub optymalizacja modelu.

6. **Publikacja i przygotowanie do wdrożenia**
   - Przygotowanie modelu do wdrożenia (np. jako API lub aplikacja internetowa).
   - Stworzenie kontenera Docker z modelem i jego zależnościami.

7. **Prezentacja i raport końcowy**
   - Przygotowanie prezentacji wyników.
   - Omówienie potencjalnych zastosowań modelu oraz jego ograniczeń.