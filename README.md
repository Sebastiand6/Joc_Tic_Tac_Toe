# Joc Tic-Tac-Toe

Acest proiect este o implementare simplă a jocului **Tic-Tac-Toe** în Python. Jocul se desfășoară între un jucător și calculator.

Jucătorul folosește simbolul **X**, iar calculatorul folosește simbolul **O**. Pentru a-și alege mutările, calculatorul folosește algoritmul **Minimax**, prin care analizează mutările disponibile și încearcă să aleagă cea mai bună variantă.

Proiectul este realizat în **consolă** și nu folosește biblioteci externe.

## Cum funcționează

La începutul jocului, tabla este afișată astfel:

```text
 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9
```

Pentru a face o mutare, jucătorul introduce numărul poziției dorite.

De exemplu:

```text
Alege o poziție (1-9): 5
```

După mutarea jucătorului, calculatorul își alege automat poziția.

Jocul continuă până când unul dintre cei doi jucători câștigă sau toate pozițiile sunt ocupate.

## Algoritmul Minimax

Calculatorul își calculează mutarea folosind algoritmul **Minimax**.

Pentru fiecare poziție disponibilă, programul simulează posibilele continuări ale jocului și atribuie un scor situației rezultate:

* **10** – câștig pentru calculator
* **-10** – câștig pentru jucător
* **0** – egalitate

Calculatorul încearcă să maximizeze scorul, în timp ce mutările jucătorului sunt evaluate astfel încât scorul să fie minimizat.

## Structura programului

Programul este împărțit în mai multe funcții, fiecare având un rol bine definit:

* `print_board()` – afișează tabla de joc
* `check_win()` – verifică dacă există un câștigător
* `check_draw()` – verifică dacă tabla este completă
* `minimax()` – implementează algoritmul Minimax
* `execute_player_move()` – citește și validează mutarea jucătorului
* `execute_computer_move()` – determină și execută mutarea calculatorului
* `play_game()` – gestionează desfășurarea jocului
* `main()` – inițializează jocul și afișează rezultatul final

## Rezultate posibile

La finalul jocului, programul poate afișa unul dintre următoarele rezultate:

```text
Ai câștigat!
```

```text
Computerul a câștigat!
```

sau:

```text
Egalitate!
```

Proiect realizat în scop educațional.
