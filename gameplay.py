# Importez la fonction
from src.utils import generate_coordinates, calculate_distance
from src.visualization import plot_country_borders
from src.georoulette import find_closest_country

DATA_path = "DATA/ne_50m_admin_0_countries.shp"


# Define language choice function with default to English after 3 incorrect attempts
def choose_language():
    attempts = 0
    language = ""
    while attempts < 3:
        language_choice = input(
            "Choose a language (enter 'fr' for French or 'en' for English): ").strip().lower()

        if language_choice == "fr":
            language = "fr"
            break
        elif language_choice == "en":
            language = "en"
            break
        else:
            attempts += 1
            if attempts < 3:
                print("Choix de langue invalide. Veuillez entrer 'fr' pour le français ou 'en' pour l'anglais.")
            else:
                print("Choix de langue invalide après 3 tentatives. Passage par défaut à l'anglais.")
                language = "en"
                break

    return language

def play_round(num_players, language):
    # Generate coordinates
    latitude, longitude = generate_coordinates()

    # Initialize scores
    scores = [0] * num_players

    # Initialize a list to store the guesses
    guesses = []

    # Ask each player to make a guess
    for i in range(num_players):
        if language == "fr":
            guess = input(f"Joueur {i + 1}, quel est le pays le plus proche ? Entrez le nom du pays : ")
        else:
            guess = input(f"Player {i + 1}, what is the closest country? Enter the country's name: ")
        guesses.append(guess.lower())

    # Find the closest country
    closest_country = find_closest_country(latitude, longitude, DATA_path)

    # Check if each guess is correct and update the scores
    for i in range(num_players):
        if guesses[i] == closest_country.lower():
            if language == "fr":
                print(f"Bravo Joueur {i + 1} ! Vous avez deviné correctement !")
            else:
                print(f"Good job, Player {i + 1}! You guessed correctly!")
            scores[i] = 1
        else:
            if language == "fr":
                print(f"Désolé Joueur {i + 1}, vous n'avez pas deviné correctement.")
            else:
                print(f"Sorry, Player {i + 1}, you didn't guess correctly.")

    # Print the correct country
    if language == "fr":
        print(f"Le pays le plus proche était : {closest_country}")
    else:
        print(f"The closest country was: {closest_country}")

    # Plot the country borders with the correct country highlighted
    plot_country_borders(latitude, longitude, DATA_path, closest_country)

    return scores


def play_georoulette(num_rounds, num_players):
    # Get the language choice
    language = choose_language()

    # Initialize scores dictionary
    scores = {f"Joueur {i + 1}": 0 for i in range(num_players)}

    # Loop through rounds
    for i in range(num_rounds):
        if language == "fr":
            print(f"\nTour {i + 1} :")
        else:
            print(f"\nRound {i + 1}:")

        round_scores = play_round(num_players, language)
        for j, score in enumerate(round_scores):
            scores[f"Joueur {j + 1}"] += score

    # Print final scores
    if language == "fr":
        print("\nScores finaux :")
    else:
        print("\nFinal Scores:")

    for player, score in scores.items():
        if language == "fr":
            print(f"{player} - {score} points")
        else:
            print(f"{player} - {score} points")


def help():
    language = choose_language()
    if language == "fr":
        print("Instructions GeoRoulette :")
        print("Le but du jeu est de deviner dans quel pays vous vous trouvez en se basant sur les coordonnées géographiques.")
        print("Un point est généré aléatoirement et vous devez deviner le pays dans lequel il se trouve.")
        print("Chaque joueur a droit à un tour.")
        print("Le joueur qui devine le pays correctement gagne un point.")
        print("Si personne ne devine le pays correctement, personne ne gagne de point.")
        print("A la fin de chaque tour, la carte du monde est affichée avec le point généré en rouge.")
        print("Le joueur avec le plus de points à la fin de tous les tours est le gagnant.")
        print("Bonne chance !")
    else:
        print("GeoRoulette Instructions:")
        print("The goal of the game is to guess which country you are in based on geographical coordinates.")
        print("A point is generated randomly, and you must guess the country where it is located.")
        print("Each player is allowed one guess.")
        print("The player who correctly guesses the country earns a point.")
        print("If no one guesses the country correctly, no one earns a point.")
        print("At the end of each round, a world map is displayed with the generated point in red.")
        print("The player with the most points at the end of all rounds is the winner.")
        print("Good luck!")

