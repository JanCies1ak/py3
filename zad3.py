import random
import getpass

number_of_rounds = int(input("Wybierz ilość rund:\n"))

game_type = input("Wybierz tryb gry\nkomputer(k)/2 gracze(g):\n")

while game_type not in ("k", "g"):
    game_type = input("Niepoprawne dane!\n")

who_won = []

first_player_name = ''
second_player_name = 'komputer'

if game_type == 'k':
    first_player_name = input('Prosze wpisać swoje imie:\n')
else:
    first_player_name = input('Gracz 1, prosze wpisać swoje imie:\n')
    second_player_name = input('Gracz 2, prosze wpisać swoje imie:\n')

first_player_move = ''
second_player_move = ''

rezults = {
    ("papier", "papier"): 0,
    ("papier", "nożyce"): 2,
    ("papier", "kamień"): 1,
    ("nożyce", "papier"): 1,
    ("nożyce", "nożyce"): 0,
    ("nożyce", "kamień"): 2,
    ("kamień", "papier"): 2,
    ("kamień", "nożyce"): 1,
    ("kamień", "kamień"): 0
}

first_player_wins = 0
second_player_wins = 0

for i in range(0, number_of_rounds):
    if game_type == 'k':
        second_player_move = random.randint(1, 3)
        if second_player_move == 1:
            second_player_move = "papier"
        elif second_player_move == 2:
            second_player_move = "nożyce"
        else:
            second_player_move = "kamień"

        first_player_move = input("Prosze wpisać swój ruch\n"
                                  "papier/nożyce/kamień:\n")

        while first_player_move not in ['papier', 'nożyce', 'kamień']:
            first_player_move = input("Niepoprawny ruch!\n")

    else:
        first_player_move = getpass.getpass(f"{first_player_name}, rosze wpisać swój ruch\n"
                                  "papier/nożyce/kamień:\n")

        while first_player_move not in ['papier', 'nożyce', 'kamień']:
            first_player_move = getpass.getpass(f"{first_player_name}, niepoprawny ruch!\n")

        second_player_move = getpass.getpass(f"{second_player_name}, rosze wpisać swój ruch\n"
                                  "papier/nożyce/kamień:\n")

        while second_player_move not in ['papier', 'nożyce', 'kamień']:
            second_player_move = getpass.getpass(f"{second_player_name}, niepoprawny ruch!\n")

        print(f"Ruchy:\n"
              f"{first_player_name}: {first_player_move}\n"
              f"{second_player_name}: {second_player_move}")

    rez = rezults.get((first_player_move, second_player_move))
    if rez == 0:
        who_won.append(f"{first_player_move} - {second_player_move}: remis")
    elif rez == 1:
        who_won.append(f"{first_player_move} - {second_player_move}: {first_player_name}")
        first_player_wins += 1
    else:
        who_won.append(f"{first_player_move} - {second_player_move}: {second_player_name}")
        second_player_wins += 1

print("Wyniki rund:")
for i in range(0, len(who_won)):
    print(f"{i}: {who_won[i]}")

print("Końcowy wynik:", end=" ")
if first_player_wins > second_player_wins:
    print(f"{first_player_name} wygrał!")
elif first_player_wins < second_player_wins:
    print(f"{second_player_name} wygrał!")
else:
    print("remis!")
