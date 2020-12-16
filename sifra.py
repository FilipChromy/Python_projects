alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphabet_length = len(alphabet)


def zasifrovani():


    text = input("Zadej text k sifrovani: ")
    klic = int(input("Zadej klíč k sifrovani: "))

    chars = []
    chars[:] = text
    output = ""

    for char in chars:
        if char == " ":
            output += " "
        elif (char not in alphabet) or (char.islower()):
            pass
        else:    
            index = alphabet.index(char)
            index_plus = (index + klic)
            while (index_plus > 25):
                index_plus -= alphabet_length

            output += alphabet[index_plus]

    print(output)


def rozsifrovani():


    text = input("Zadej zasifrovany text: ")
    klic = int(input("Zadej klic k desifrovani: "))

    chars = []
    chars[:] = text
    output = ""

    for char in chars:
        if char == " ":
            output += " "
        elif (char not in alphabet) or (char.islower()):
            pass
        else:
            index = alphabet.index(char)
            index_minus = index - klic
            while (index_minus < 0):
                index_minus += alphabet_length
                
            output += alphabet[index_minus]
        
    print(output)


dotaz = input("Zadejte 0 pro ZASIFROVANI nebo 1 pro DESIFROVANI: ")

if dotaz == "0":
    zasifrovani()
elif dotaz == "1":
    rozsifrovani()   
else:
    print("Spatne zadana hodnota!")
