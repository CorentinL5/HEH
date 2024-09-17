iban = input("Entrer un IBAN, svp: ")
iban = iban.replace(' ','')
if not iban.isalnum():
    print("Vous avez entré un caractère non valide.")
elif len(iban) < 15:
    print("IBAN entrer est trop court.")
elif len(iban) > 31:
    print("IBAN entrer est trop long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
    else:
        iban2 += str(10 + ord(ch) - ord('A'))
        iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entrer est valide.")
    else:
        print("IBAN entrer est invalide.")