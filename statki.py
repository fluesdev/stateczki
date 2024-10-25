from random import randint

# Tworze plansze 5x5 z "O" oznaczającymi wolne pola
board = []
for x in range(0, 5):
    board.append(["O"] * 5)

# Funkcja do wyświetlania planszy
def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)

# Funkcja losująca wiersz dla statku
def random_row(board):
    return randint(0, len(board) - 1)

# Funkcja losująca kolumnę dla statku
def random_col(board):
    return randint(0, len(board[0]) - 1)

# Losowa lokalizacja statku
ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)  # Wydrukuj położenie statku dla testów
print(ship_col)

# Rozpoczęcie gry na 4 tury
for turn in range(4):
    print("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Arrr, zatopiles mnie")
        break  # Koniec gry po trafieniu
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print("To jest poza oceanem kamracie")
        elif board[guess_row][guess_col] == "X":
            print("Tu juz strzelales kamracie")
        else:
            print("Pudlo!")
            board[guess_row][guess_col] = "X"
        
        # Sprawdzenie, czy to była ostatnia tura
        if turn == 3:
            print("koniec gry")
        print_board(board)
