

def laske_yksikkohinta(halkaisija, hinta): #ottaa halkaisijan senttimetreinä
    #ympyrän pinta-alan kaavaa   #pi arvo
    pizzan_pinta_ala = 3.14159 * (halkaisija / 2) ** 2
    #pizzan hita jaettuna pinta-ala
    yksikkohinta = hinta / pizzan_pinta_ala
    # tulosta ja lopettaa funktion suorituksen
    return yksikkohinta

#kutsuu pääohjelmaa
def main():         #luku liukuluvuksi
    halkaisija1 = float(input("Syötä ensimmäisen pizzan halkaisija senttimetreinä: "))
    hinta1 = float(input("Syötä ensimmäisen pizzan hinta euroina: "))
    halkaisija2 = float(input("Syötä toisen pizzan halkaisija senttimetreinä: "))
    hinta2 = float(input("Syötä toisen pizzan hinta euroina: "))
    #kertoo kumpi on halvempi
    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

    if yksikkohinta1 < yksikkohinta2: # vertailee pizzan yksikköhinta
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif yksikkohinta2 < yksikkohinta1:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmat pizzat antavat saman vastineen rahalle.")


if __name__ == "__main__":
    main()
