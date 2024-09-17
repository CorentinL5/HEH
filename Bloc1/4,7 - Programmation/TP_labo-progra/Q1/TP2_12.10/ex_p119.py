inputBlocks = int(input("De combien de blocks disposez vous ?\n =>"))
prev = 0
i = 1
pyramidHeight = 0
while (inputBlocks >= 0):
    pyramidHeight += 1
    inputBlocks -= i - prev
    i, prev = i + prev, i
    print(prev, i)

print(pyramidHeight)