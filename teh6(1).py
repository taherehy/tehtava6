


import random     #kirjasto

def heita_noppaa():                      #määritää tulos ja heitoa.
    return random.randint(1, 6)          #tulosta random numeroita1-6.

def main():               #nopanheittoa ja tulostaa
    while True: #silmukka
        silmaluku = heita_noppaa() #antaa luku 1_6 väliltä .

        print("Heitto:", silmaluku)

        if silmaluku == 6:                     #onko luku yhtä suuri kuin 6
            print("Kuutonen! Lopetetaan heittäminen.")

            break                               #jos on 6 arvonen lopetaa

if __name__ == "__main__": # suorittaa
                        #ohjelmasi joko moduulina tai suoraan
    main()
