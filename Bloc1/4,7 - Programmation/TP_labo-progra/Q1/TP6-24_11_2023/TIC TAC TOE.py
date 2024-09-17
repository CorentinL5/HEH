# TicTacToe By CorentinL. ----> non terminé

# init
game_is_started = False
box_of_grid = ["1", "2", "3", "4", "X", "6", "7", "8", "9"]
whosplaying = ["Ø", "X"]


def showgrid():
    print("")
    print("       |       |")
    print("  ", box_of_grid[0], "  |  ", box_of_grid[1], "  |  ", box_of_grid[2])
    print("_______|_______|_______")
    print("       |       |")
    print("  ", box_of_grid[3], "  |  ", box_of_grid[4], "  |  ", box_of_grid[5])
    print("_______|_______|_______")
    print("       |       |")
    print("  ", box_of_grid[6], "  |  ", box_of_grid[7], "  |  ", box_of_grid[8])
    print("       |       |")


def startgame():
    global game_is_started
    input('Appuyer sur "Enter" quand vous êtes prêt pour commencer le jeu.')
    game_is_started = True

def bottoplay():
    pass



# EndGame
def endgame():
    pass  # Add your end game logic here


# Main game loop
while not game_is_started:
    startgame()

while game_is_started:
    print('Entrez la case que vous voulez remplir avec votre "O"')
    choice_of_player = input("=>")
    try:
        index = int(choice_of_player) - 1
        if index < 0 or index >= len(box_of_grid):
            print("La case sélectionnée n'est pas valide!")
            continue

        if box_of_grid[index] in whosplaying:
            print("La case est déjà prise!")
            continue

        box_of_grid[index] = whosplaying[0]
    except ValueError:
        print("Ce n'est pas un chiffre valide!")
        continue

    bottoplay()
    showgrid()

    # Add your win/lose conditions and call endgame() when needed

# Optionally, you can call endgame() after the loop if there's any cleanup or final messages you want to display
endgame()
