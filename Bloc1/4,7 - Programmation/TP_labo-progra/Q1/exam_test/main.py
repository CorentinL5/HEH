import os

def find_txt_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            #print(file)
            if file.endswith('.txt'):
                yield os.path.join(root, file)

def find_word_function(wordToFind):
    wordFindeddico = {}
    for path in find_txt_files('./'):
        with open(path, "r", encoding="utf-8") as openFile:
            for line in openFile:
                wordFindeddico[path] = wordFindeddico.get(path, 0) + line.count(wordToFind)
    return wordFindeddico


tempDico = find_word_function("mot_a_trouver")
tempList = ""
for i in (tempDico):
    if tempDico[i] != 0:
        tempList += (i + " ")

def trier():
    files = {}
    for path in find_txt_files("./"):
        files[path] = os.path.getsize(path)
    sorted_files = sorted(files.items(), key= lambda x :x[1], reverse = True)
    for key in sorted_files:
        print(key)


def lzw(s):
    dico = {}
    for i in range(256):
        dico[chr(i)] = i
    res = []
    w = ""
    for c in s:
        wc = w + c
        if wc in dico:
            w = wc
        else:
            res.append(dico[w])
            dico[wc] = len(dico)
            w = c
    if w:
        res.append(dico[w])
    return res

