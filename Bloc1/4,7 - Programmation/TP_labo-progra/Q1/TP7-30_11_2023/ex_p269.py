def mysplit(strng):
    if not strng:
        return []

    words = []
    current_word = ''

    for char in strng:
        if char.isspace():
            if current_word:
                words.append(current_word)
                current_word = ''
        else:
            current_word += char

    if current_word:
        words.append(current_word)

    return words


print(mysplit("Être ou ne pas être, telle est la question"))
print(mysplit("Être ou ne pas être,telle est la question "))
print(mysplit(" "))
print(mysplit(" abc "))
print(mysplit(""))

# ['Etre','ou', ’ne’, 'pas', 'être, 'telle', 'est', 'la', 'question']
# ['Etre','ou', ’ne’, 'pas', 'être,telle', 'est', 'la', 'question'] []
# ['abc']
# []
