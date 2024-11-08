import random
import os

# Toont een bericht in een vakje om het leesbaar te maken
def print_vakje(tekst):
    lengte = len(tekst) + 4  # Zorgt dat het vakje past bij de tekstlengte
    print("+" + "-" * (lengte - 2) + "+")
    print(f"|  {tekst}  |")
    print("+" + "-" * (lengte - 2) + "+")

# Functie voor het raadspel
def raadspel():
    print_vakje("🚀 Welkom bij het Ruimte Raadspel! ⭐️")
    max_number = 20  # Het hoogste getal dat geraden moet worden
    max_guesses = 5  # Het aantal pogingen dat de speler heeft
    number = random.randint(1, max_number)  # Genereert een willekeurig getal

    # Laat zien welk getal gezocht wordt en hoeveel pogingen er zijn
    print_vakje(f"Ik heb een magisch getal gekozen tussen 1 en {max_number}. 🌌")
    print_vakje(f"Je hebt {max_guesses} kansen om het te raden! 🌟")

    # De speler kan meerdere keren raden om het getal te vinden
    for attempt in range(1, max_guesses + 1):
        # Toont het huidige aantal pogingen
        print(f"""\n
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ ✨ Poging {attempt}: Wat is je gok? 💭     ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)

        # Vraagt om een getal en controleert of het geldig is
        try:
            guess = int(input("Voer je gok in: "))
        except ValueError:
            print_vakje("🚫 Ongeldige invoer! Voer een geldig getal in.")
            continue  # Ga door naar de volgende poging als het geen getal was

        # Controleert of de gok te hoog, te laag of juist is
        if guess < number:
            remaining_attempts = max_guesses - attempt
            print_vakje(f"Te laag! 📉 Nog {remaining_attempts} pogingen.")
        elif guess > number:
            remaining_attempts = max_guesses - attempt
            print_vakje(f"Te hoog! 📈 Nog {remaining_attempts} pogingen.")
        else:
            # De speler heeft het juiste getal geraden
            print_vakje(f"🎉 Gefeliciteerd! Je hebt het magische getal {number} geraden in {attempt} pogingen! 🌟🚀")
            break
    else:
        # De speler heeft al zijn pogingen gebruikt en het getal niet geraden
        print_vakje(f"Helaas, het getal was {number}. Volgende keer beter! 💔")

# Functie voor het Galgje spel waarin de speler een woord moet raden
def galgje():
    bestandsnaam = 'woordenlijst.txt'

    # Controleert of de woordenlijst bestaat en maakt er een als die ontbreekt
    if not os.path.exists(bestandsnaam):
        with open(bestandsnaam, 'w') as bestand:
            bestand.write("# makkelijk\nplaneet\nmaan\nster\nzon\n")
            bestand.write("\n# gemiddeld\nsterrenstelsel\nkometen\nmeteoor\nruimtestation\n")
            bestand.write("\n# moeilijk\nzonnestelsel\nastronaut\nsatelliet\nzwaartekracht\n")
        print_vakje(f"Woordenlijst '{bestandsnaam}' aangemaakt met standaard woorden. 🌌")

    # De status van de speler wordt weergegeven
    ruimte_stadia = [
        "🚀🌍🌑🌑🌑🌑🌑   - De raket staat klaar op de lanceerbasis.",
        "🚀🌕🌑🌑🌑🌑🌑   - De raket stijgt op! 🚀",
        "🚀🌕🌕🌑🌑🌑🌑   - De raket gaat richting de sterren! ✨",
        "🚀🌕🌕🌕🌑🌑🌑   - Halverwege naar de ruimte! 🌌",
        "🚀🌕🌕🌕🌕🌑🌑   - Bijna in de ruimte... 🌠",
        "🚀🌕🌕🌕🌕🌕🌑   - De raket heeft de ruimte bereikt! 🌍✨",
        "💥💥💥💥💥💥     - O nee! De raket is geëxplodeerd in de ruimte! 😢"
    ]

    # Laad woorden in drie moeilijkheidsgraden
    woorden = {'makkelijk': [], 'gemiddeld': [], 'moeilijk': []}
    huidige_categorie = None

    # Woorden worden uit het bestand geladen en in de juiste categorie gezet
    with open(bestandsnaam, 'r') as bestand:
        for lijn in bestand:
            lijn = lijn.strip()

        
        # Startswith controleert of de regel begint met een bepaald stuk tekst.
        # In dit geval kijkt het of de regel begint met '# makkelijk
            if lijn.startswith('# makkelijk'):
                huidige_categorie = 'makkelijk'
            elif lijn.startswith('# gemiddeld'):
                huidige_categorie = 'gemiddeld'
            elif lijn.startswith('# moeilijk'):
                huidige_categorie = 'moeilijk'

            # Als de regel een woord bevat (niet leeg) en er is al een categorie ingesteld
            elif lijn and huidige_categorie:
            # Voeg het woord toe aan de juiste categorie in de woordenlijst

                woorden[huidige_categorie].append(lijn)

    # Introductie voor het Galgje spel
    print_vakje("🌌 Welkom bij Galgje: Ruimte Editie! 🚀")
    naam = input("Wat is je naam, astronaut? 👨‍🚀 ")

    # De speler kiest een moeilijkheidsgraad
    moeilijkheid = ""
    while moeilijkheid not in ['makkelijk', 'gemiddeld', 'moeilijk']:
        print("""\n
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ Kies een moeilijkheidsgraad:               ┃
        ┃ 1. Makkelijk 🪐                            ┃
        ┃ 2. Gemiddeld 🚀                           ┃
        ┃ 3. Moeilijk 🌌                            ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """)
        moeilijkheid = input("Kies je moeilijkheidsgraad (makkelijk, gemiddeld, moeilijk): ").lower()

    # Kies een willekeurig woord op basis van de moeilijkheidsgraad
    woord = random.choice(woorden[moeilijkheid])
    goed_geraden = []  # Lijst van letters die correct zijn geraden
    fout_geraden = []  # Lijst van letters die fout zijn geraden
    pogingen = 6  # Het aantal keer dat je fout mag raden

    # Start van het Galgje spel
    while pogingen > 0:
        # Laat zien hoever de speler is met het spel
        print("\n" + ruimte_stadia[6 - pogingen])
        
        # Bouw het woord op met goed geraden letters en streepjes voor ontbrekende letters
        woord_weergave = ''
        for letter in woord:
            if letter in goed_geraden:
                woord_weergave += letter + ' '
            else:
                woord_weergave += '_ '
        print_vakje(f"Woord: {woord_weergave.strip()}")

        # Vraag de speler om een letter te raden
        gok = input("Raad een letter: ").lower()

        # Controleert of de invoer geldig is
        if len(gok) != 1 or not gok.isalpha():
            print_vakje("🚫 Ongeldige invoer, probeer opnieuw.")
            continue

        # Controleert of de letter al eerder is geraden
        if gok in goed_geraden or gok in fout_geraden:
            print_vakje(f"🔄 '{gok}' is al geraden.")
            continue

        # Voeg de letter toe aan goed of fout, afhankelijk van of deze in het woord zit
        if gok in woord:
            goed_geraden.append(gok)
            print_vakje(f"🎉 Goed zo! '{gok}' zit in het woord.")
        else:
            fout_geraden.append(gok)
            pogingen -= 1
            print_vakje(f"❌ Helaas, '{gok}' zit niet in het woord. Pogingen over: {pogingen}")

        # Controleert of het hele woord is geraden
        volledig_woord_geraden = True
        for letter in woord:
            if letter not in goed_geraden:
                volledig_woord_geraden = False
                break

        # Laat weten dat het hele woord is geraden
        if volledig_woord_geraden:
            print_vakje(f"🎊 Gefeliciteerd, {naam}! Het woord was '{woord}'! 🚀")
            break
    else:
        # De speler heeft al zijn pogingen gebruikt en het woord niet geraden
        print(ruimte_stadia[6])
        print_vakje(f"Helaas, je hebt geen pogingen meer. Het woord was '{woord}'.")

    print_vakje("Bedankt voor het spelen! Tot de volgende keer! 🌌")

# Functie die het hoofdmenu toont voor het kiezen van een spel
def hoofdmenu():
    print("""\n
    ┏━━━━━━━━━━━━━━━━━━━━━✦✧✦━━━━━━━━━━━━━━━━━━━━━┓
             🌟 Hoofdmenu 🌌
    ┗━━━━━━━━━━━━━━━━━━━━━✦✧✦━━━━━━━━━━━━━━━━━━━━━┛
    
    Kies een spel:
    ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
    ┃ 1. Raadspel 🌠                             ┃
    ┃ 2. Galgje: Ruimte Editie 🚀                ┃
    ┃ 3. Stoppen 🛑                              ┃
    ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """)
    keuze = input("Maak je keuze (1-3): ")
    return keuze

# Start het spel
while True:
    # Hoofdmenu loopt door totdat de gebruiker wil stoppen
    keuze = hoofdmenu()
    if keuze == '1':
        print_vakje("🌟 Start Raadspel! 🚀")
         # Roept de functie aan die het Raadspel start
        raadspel()
    elif keuze == '2':
        print_vakje("🌟 Start Galgje: Ruimte Editie! 🚀")
        # Roept de functie aan die het Galgje spel start
        galgje()
    elif keuze == '3':
        print_vakje("Bedankt voor het spelen! Tot de volgende keer!")
        # Stopt de lus om het spel af te sluiten
        break
    else:
        print_vakje("🚫 Ongeldige keuze, probeer het opnieuw.")


    















