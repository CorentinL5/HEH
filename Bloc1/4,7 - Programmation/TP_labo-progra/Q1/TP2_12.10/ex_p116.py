userInput = input("Entrez un mot (si c'est chupacabra cella arrête le programme").upper()

while (userInput != "chupacabra"):
    for letter in userInput:
        print(letter, end="")
    userInput = input("\nUn autre mot ?").upper()