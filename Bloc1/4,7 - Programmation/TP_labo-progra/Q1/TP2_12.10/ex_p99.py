income = float(input("enter the annual income: "))


if (income <= 82528):
    tax = income * 0.18 - 556.2
else: # pas bon
    tax = income * 0.32
    if (tax < 14839.2): tax = 14839.2




tax : int(round(tax, 0))
print("The tax is : ", tax, "Funcoins")




