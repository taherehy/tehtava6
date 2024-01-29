

def gallonat_litroiksi(gallonat):
    return gallonat * 3.785

while True: #koodi toistaa itsensä loputtomasti
    #merkkijono---> liukulukuksi
    gallonat = float(input("Syötä bensiinin määrä gallonoina (negatiivinen luku lopettaa): "))

    if gallonat < 0: #onko negativinin syöte
        print("Lopetetaan muuntaminen.")
        break #lopetaa
    print(f"{gallonat} nestegallonaa on {gallonat_litroiksi(gallonat):.2f} litraa.")
            #f desimaalina tuosta          #muuttujan arvon litroina     # tulostetaan kahden