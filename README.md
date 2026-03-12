# Chess Engine & GUI ♟️

Silnik szachowy zbudowany w Pythonie z wykorzystaniem biblioteki Pygame. Projekt obejmuje pełną logikę gry, interfejs graficzny oraz algorytmy sztucznej inteligencji.

## 🚀 Główne Funkcjonalności

- **Pełna Logika Szachowa**: Obsługa wszystkich zasad, w tym:
  - Roszada (krótka i długa).
  - Bicie w przelocie (*En Passant*).
  - Promocja pionka z interaktywnym menu wyboru figury.
  - Wykrywanie szacha, matu oraz pata.
- **Silnik AI**: Trzy poziomy trudności:
  - **Level 0 (Random)**: Wybór losowych legalnych ruchów.
  - **Level 1 (Greedy)**: Algorytm zachłanny optymalizujący wartość materiału.
  - **Level 2 (Negamax)**: Algorytm przeszukiwania drzewa gry z przewidywaniem ruchów przeciwnika. (w trakcie tworzenia)
- **Interfejs Graficzny**: 
  - Renderowanie planszy i zestawu figur w 60 FPS.
  - Dynamiczny pasek statusu informujący o turze i stanie gry.
  - System podświetlania legalnych ruchów dla wybranej figury.

## 🛠️ Technologie

- **Język**: Python 3.13
- **Biblioteka GUI**: Pygame 2.6
- **Architektura**: Model-View-Controller (MVC) z wyraźnym oddzieleniem logiki silnika (`engine`) od warstwy wizualnej (`visuals`).

## 🧠 Algorytmy i Optymalizacja

W projekcie zaimplementowano zaawansowane techniki programistyczne:
- **Rekurencja**: Wykorzystywana w algorytmie Negamax do symulacji przyszłych stanów planszy.
- **Wirtualne Ruchy**: ystem `is_virtual`, pozwalający AI na testowanie tysięcy kombinacji bez modyfikowania rzeczywistego stanu gry.
- **Zarządzanie Pamięcią**: Optymalizacja poprzez śledzenie list aktywnych figur (`white_pieces`, `black_pieces`), co drastycznie przyspiesza funkcję ewaluacyjną.

## 📦 Instalacja i Uruchomienie

1. Sklonuj repozytorium:
   ```bash
   git clone [https://github.com/dzejchym21/chess-project.git]