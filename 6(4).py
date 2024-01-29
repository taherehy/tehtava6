"Funktio laskee annetun listan lukujen summan."

def laske_summa(lista):
    return sum(lista)

def main(): #luo listan
    lista = [1, 2, 3, 4, 5]
    summa = laske_summa(lista) #kutsuu summafunktiota
    print("Listan summa on:", summa)  #tulosta summa

if __name__ == "__main__":
    main()
