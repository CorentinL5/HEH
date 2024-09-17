secretNumber = 777
numberInput = int(input(
    """
    +===================================+
    | Welcome to my game, muggle        |
    | Enter an integrer number          |
    | and guess what number I've        |
    | picked for you                    |
    | So, what's the secret number?     |
    +===================================+
    =>""")
)
while (numberInput != secretNumber):
    print("Haha,! You're stuck in my loop!")
    numberInput = int(input("So, what's the secret number?\n=>"))
print("Well played, muggle! You're frre now. Your knownledge gets closer of the Mandoux Master")


