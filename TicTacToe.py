#Herní pole
row1 = ["   ", "|", "   ", "|", "   "]
row2 = ["___", "_", "___", "_", "___"]
row3 = ["   ", "|", "   ", "|", "   "]
row4 = ["___", "_", "___", "_", "___"]
row5 = ["   ", "|", "   ", "|", "   "]

#Vygenerování herního pole
def build_game_field():
    print("\n")
    print(*row1, sep= "")
    print(*row2, sep= "")
    print(*row3, sep= "")
    print(*row4, sep= "")
    print(*row5, sep= "")
    print("\n")

playable_positions = ["pos1", "pos2", "pos3", "pos4", "pos5", "pos6", "pos7", "pos8", "pos9"]


while True:
    build_game_field()
    while True:
        x = input(f"X plays! Where do you want to play? {playable_positions}: ")
        if x not in playable_positions:
            print("Not a valid position")
            continue
        else:
            if x == "pos1":
                row1[0] = " X "
            elif x == "pos2":
                row1[2] = " X "
            elif x == "pos3":
                row1[4] = " X "    
            elif x == "pos4":
                row3[0] = " X "
            elif x == "pos5":
                row3[2] = " X "
            elif x == "pos6":
                row3[4] = " X "
            elif x == "pos7":
                row5[0] = " X "
            elif x == "pos8":
                row5[2] = " X "
            elif x == "pos9":
                row5[4] = " X "
            playable_positions.remove(x)
            break
    
    build_game_field()
    
    if row1[0] == " X " and row1[2] == " X " and row1[4] == " X ":
        print("X wins!")
        break
    elif row5[0] == " X " and row5[2] == " X " and row5[4] == " X ":
        print("X wins")
        break
    elif row1[0] == " X " and row3[0] == " X " and row5[0] == " X ":
        print("X Wins")
        break
    elif row1[4] == " X " and row3[4] == " X " and row5[4] == " X ":
        print("X wins")
        break
    elif row1[0] == " X " and row3[2] == " X " and row5[4] == " X ":
        print("X wins")
        break
    elif row1[4] == " X " and row3[2] == " X " and row5[0] == " X ":
        print("X wins")
        break
    elif row1[2] == " X " and row3[2] == " X " and row5[2] == " X ":
        print("X wins")
        break
    elif row3[0] == " X " and row3[2] == " X " and row3[4] == " X ":
        print("X wins")
        break
    


    while True:
        y = input(f"Y plays! Where do you want to play? {playable_positions}: ")
        if y not in playable_positions:
            print("Not a valid position")
            continue
        else:
            if y == "pos1":
                row1[0] = " Y "
            elif y == "pos2":
                row1[2] = " Y "
            elif y == "pos3":
                row1[4] = " Y "    
            elif y == "pos4":
                row3[0] = " Y "
            elif y == "pos5":
                row3[2] = " Y "
            elif y == "pos6":
                row3[4] = " Y "
            elif y == "pos7":
                row5[0] = " Y "
            elif y == "pos8":
                row5[2] = " Y "
            elif y == "pos9":
                row5[4] = " Y "
            playable_positions.remove(y)
            break
    
    build_game_field()

    if row1[0] == " Y " and row1[2] == " Y " and row1[4] == " Y ":
        print("Y wins!")
        break
    elif row5[0] == " Y " and row5[2] == " Y " and row5[4] == " Y ":
        print("Y wins")
        break
    elif row1[0] == " Y " and row3[0] == " Y " and row5[0] == " Y ":
        print("Y Wins")
        break
    elif row1[4] == " Y " and row3[4] == " Y " and row5[4] == " Y ":
        print("Y wins")
        break
    elif row1[0] == " Y " and row3[2] == " Y " and row5[4] == " Y ":
        print("Y wins")
        break
    elif row1[4] == " Y " and row3[2] == " Y " and row5[0] == " Y ":
        print("Y wins")
        break
    elif row1[2] == " Y " and row3[2] == " Y " and row5[2] == " Y ":
        print("Y wins")
        break
    elif row3[0] == " Y " and row3[2] == " Y " and row3[4] == " Y ":
        print("Y wins")
        break