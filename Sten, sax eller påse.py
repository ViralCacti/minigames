print("Sten, sax, påse ~ ViralCactus")

import random
import time

def gameEngine():

    valAvTNGT = int(input("\nVilken input vill du spela med; bokstäver eller siffror?\n\t"
                          "[1]: Bokstäver\n\t"
                          "[2]: Siffor\n"
                          "Ange ID här: >> "))

    if valAvTNGT == 1:
        DEFdragAnvändare = input("\nSten, sax eller påse? [Ange svaret i gemener] >> ")

        DEFdragMöjliga = ["sten", "sax", "påse"]
        DEFdragAI = random.choice(DEFdragMöjliga)

        print(f"\tDitt drag: {DEFdragAnvändare}\n\tAI:s drag: {DEFdragAI}\n")

        if DEFdragMöjliga == DEFdragAI:
            print("Oavgjort.")

        elif DEFdragAnvändare == "sten":
            if DEFdragAI == "påse":
                print("Du förlorade.")
            elif DEFdragAI == "sten":
                print("Oavgjort.")
            else:
                print("Du vann!")

        elif DEFdragAnvändare == "påse":
            if DEFdragAI == "sax":
                print("Du förlorade.")
            elif DEFdragAI == "påse":
                print("Oavgjort.")
            else:
                print("Du vann!")

        elif DEFdragAnvändare == "sax":
            if DEFdragAI == "sten":
                print("Du förlorade.")
            elif DEFdragAI == "sax":
                print("Oavgjort.")
            else:
                print("Du vann!")

        spelaIgenInput1 = input("\nAI: Tack för en god match. Vill du spela igen?\n\tJ för ja, N för nej: >> ")
        if spelaIgenInput1 == "J":
            gameEngine()
        else:
            print("\n\to/")
            time.sleep(1)
            quit()

    if valAvTNGT == 2:
        DEFdragAnvändare2 = int(input("\nSten [1], sax [2] eller påse [3]? >> "))

        DEFdragMöjliga2 = ["sten", "sax", "påse"]
        DEFdragAI2 = random.choice(DEFdragMöjliga2)

        if DEFdragAnvändare2 == 1:
            print(f"\tDitt drag: Sten\n\tAI:s drag: {DEFdragAI2}\n")
            if DEFdragAI2 == "påse":
                print("Du förlorade.")
            elif DEFdragAI2 == "sten":
                print("Oavgjort.")
            else:
                print("Du vann!")
        elif DEFdragAnvändare2 == 2:
            print(f"\tDitt drag: Sax\n\tAI:s drag: {DEFdragAI2}\n")
            if DEFdragAI2 == "sten":
                print("Du förlorade.")
            elif DEFdragAI2 == "sax":
                print("Oavgjort.")
            else:
                print("Du vann!")
        elif DEFdragAnvändare2 == 3:
            print(f"\tDitt drag: Påse\n\tAI:s drag: {DEFdragAI2}\n")
            if DEFdragAI2 == "sax":
                print("Du förlorade.")
            elif DEFdragAI2 == "påse":
                print("Oavgjort.")
            else:
                print("Du vann!")

        spelaIgenInput2 = int(input("\nAI: Tack för en god match. Vill du spela igen?\n\t[1] för JA \n\t[2] för NEJ \n>> "))
        if spelaIgenInput2 == 1:
            gameEngine()
        else:
            print("\n\to/")
            time.sleep(1)
            quit()


gameEngine()