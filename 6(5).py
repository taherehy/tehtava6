
def karsi_parittomat(lista): #funktion

    return [luku for luku in lista if luku % 2 == 0]
    #Se käy läpi jokaisen lukun listasta ja lisää sen tarkista parilliset


def main(): #pääohjelman
    alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 # kutsutaan funktiota
    karsittu_lista = karsi_parittomat(alkuperainen_lista)

#tulostaa alkuperäinen lista
    print("\n")
    print("Alkuperäinen lista:", alkuperainen_lista)
    print ("\n")
    print("Karsittu lista (parilliset luvut):", karsittu_lista)   # tulosta alkuperäisen listan parilliset


if __name__ == "__main__":
    main()
