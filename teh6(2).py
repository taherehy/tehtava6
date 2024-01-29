#kirjasto
import random

#funktion määritelee heita_noppaa
def heita_noppaa(tahkojen_maara):
    return random.randint(1, tahkojen_maara)

#määritelee pääohjelma
def main():
    tahkojen_maara = int(input("Syötä nopan tahkojen yhteismäärä: "))
    while True: #silmkaa
        silmaluku = heita_noppaa(tahkojen_maara) #ohjelma jatkaa ja tallenaa.
        print("Heitto:", silmaluku)

        if silmaluku == tahkojen_maara:    #tarkistaa onko luku yhtä suuri kuin tahkojen määrä
            print(f"Silmäluvun {tahkojen_maara} saaminen! Lopetetaan heittäminen.")
            break #lopetaa ohjelma

if __name__ == "__main__": #suoritaa muudle
    main()
