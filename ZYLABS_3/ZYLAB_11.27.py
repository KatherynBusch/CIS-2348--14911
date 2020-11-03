# Katheryn Busch PSID: 1868948
players = {}
jersey_numbers = []


def mainMenu():


    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print("\nChoose an option:")


def commands():

    while True:
        mainMenu()
        text = input("")
        if text == 'o':
            output_roster()
        elif text == 'a':
            add_player()
        elif text == 'd':
            delete_player()
        elif text == 'u':
            update_player()
        elif text == 'r':
            output_players_above_rating()
        elif text == 'q':
            break


def init():

    global jersey_numbers
    global players

    for j in range(5):
        jersey_number = int(input(f"Enter player {j + 1}'s jersey number:\n"))
        rating = int(input(f"Enter player {j + 1}'s rating:\n\n"))
        players[jersey_number] = rating
        jersey_numbers.append(jersey_number)

    jersey_numbers = sorted(jersey_numbers)


def output_roster():


    global jersey_numbers
    global players

    print("ROSTER")
    for j in range(len(players)):
        jersey_number = jersey_numbers[j]
        print(f"Jersey number: {jersey_number}, Rating: {players[jersey_number]}")


def add_player():


    global jersey_numbers
    global players
    jersey_number = int(input("\nEnter a new player's jersey number: "))
    rating = int(input("Enter the player's rating: "))
    players[jersey_number] = rating
    jersey_numbers.append(jersey_number)
    jersey_numbers = sorted(jersey_numbers)


def delete_player():


    global jersey_numbers
    global players
    jersey_number = int(input("\nEnter a jersey number: "))
    del players[jersey_number]
    jersey_numbers.remove(jersey_number)
    jersey_numbers.sort()


def update_player():


    global jersey_numbers
    global players
    jersey_number = int(input("\nEnter a jersey number: "))
    ratingNew = int(input("Enter a new rating for player: "))
    players[jersey_number] = ratingNew


def output_players_above_rating():

    global jersey_numbers
    global players
    min_rating = int(input("\nEnter a rating: "))
    above_rating_jersey_numbers = []

for jersey_number, rating in players.items():
    if rating > min_rating:
        above_rating_jersey_numbers.append(jersey_number)
    above_rating_jersey_numbers = sorted(above_rating_jersey_numbers)
    print(f"ABOVE {min_rating}")
    for jersey_number in above_rating_jersey_numbers:
        print(
            f"Jersey number: {jersey_number}, Rating: {players[jersey_number]}")


def main():


    global jersey_numbers
    global players
    init()
    output_roster()
    commands()
main()
