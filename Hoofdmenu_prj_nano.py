def hoofdmenu():
    while True:
        print("⫘⫘⫘⫘⫘⫘ 𝐖𝐞𝐥𝐤𝐨𝐦 𝐛𝐢𝐣 𝐀𝐩𝐩-𝐬𝐭𝐨𝐫𝐞 𝐏𝐲𝐀𝐩𝐩𝐬! ⫘⫘⫘⫘⫘⫘")
        print("Kies uw gewenste applicatie:")
        print("Optie 1: Raad het getal")
        print("Optie 2: Galgje")
        print("Optie 3: Verlaat de App-store")
        keuze = input("Voer je keuze in (1/2/3): ")

        if keuze == "1":
            import raad_het_nummer
            raad_het_nummer.raad_het_getal()
        elif keuze == "2":
            import Galgje
            Galgje.galgje()
        elif keuze == "3":
            print("Bedankt voor het spelen. Tot de volgende keer!")
            break
        elif keuze == '':
            print("Ongeldige keuze, probeer het opnieuw.")
        else:
            print("Ongeldige keuze, probeer het opnieuw.")


if __name__ == "__main__":
    hoofdmenu()


