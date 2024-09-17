print("Entrez les matricules (-1 pour arreter)")
myList = []
userInput = 0
while userInput != -1:
    myList.append(userInput)
    userInput = int(input("=>"))
del myList[0]
tempList = myList
myList = []
for i in tempList:
    if i not in myList:
        myList.append(i)
print("The list with unique elements only:\n", myList)
