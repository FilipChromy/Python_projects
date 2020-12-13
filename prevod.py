def preved(znak):
    vysledek = ""
    for i in znak:
        if i == " ":
            vysledek += i
        elif i.isdigit():
            i = int(i) + (5 % 10)
            if i >= 10:
                i = i - 10
                vysledek += str(i)
            else:
                vysledek += str(i)
        elif i.isupper() == False and i.islower() == False:
            vysledek += i
        elif i.isupper():
            vysledek += i.lower()
        elif i.islower():
            vysledek += i.upper()

    print(vysledek)



preved("AhoJ svEtE, 992")