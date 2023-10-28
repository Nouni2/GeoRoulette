from gameplay import *

def main():
    # Obtenir le choix de langue depuis gameplay.py
    language = choose_language()

    if language == "fr":
        # Texte en français
        print("Vous avez choisi le français.\n")
    else:
        # Texte en anglais
        print("You've chosen English.\n")

    # Demander le nombre de joueurs et de tours
    num_players = int(input("Combien de joueurs ? " if language == "fr" else "How many players? "))
    num_rounds = int(input("Combien de tours ? " if language == "fr" else "How many rounds? "))

    if language == "fr":
        # Texte en français
        print("Pour obtenir de l'aide, tapez 'help()' à tout moment.\n")
    else:
        # Texte en anglais
        print("To get help, type 'help()' at any time.\n")

    # Jouer le jeu pour le nombre de tours spécifié
    scores = num_players * [0]
    for i in range(num_rounds):
        if language == "fr":
            # Texte en français
            print(f"\nTour n°{i + 1} !")
        else:
            # Texte en anglais
            print(f"\nRound {i + 1}!")

        round_score = play_round(num_players, language)
        for j in range(num_players):
            scores[j] += round_score[j]

    # Trouver le joueur avec le score le plus élevé
    max_score = max(scores)
    winners = [i + 1 for i, score in enumerate(scores) if score == max_score]

    if language == "fr":
        # Texte en français
        print("\nScores finaux:")
    else:
        # Texte en anglais
        print("\nFinal Scores:")

    for i, score in enumerate(scores):
        if language == "fr":
            # Texte en français
            print(f"Joueur {i + 1}: {score}")
        else:
            # Texte en anglais
            print(f"Player {i + 1}: {score}")

    if len(winners) == 1:
        if language == "fr":
            # Texte en français
            print(f"\nLe joueur {winners[0]} a gagné avec un score de {max_score}!")
        else:
            # Texte en anglais
            print(f"\nPlayer {winners[0]} has won with a score of {max_score}!")
    else:
        if language == "fr":
            # Texte en français
            print(f"\nIl y a une égalité entre les joueurs {', '.join(map(str, winners))} avec un score de {max_score}!")
        else:
            # Texte en anglais
            print(f"\nThere's a tie between players {', '.join(map(str, winners))} with a score of {max_score}!")

if __name__ == "__main__":
    main()