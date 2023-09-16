#Sangheftegenerator

import pandas as pd
import random
from googlesearch import search
import requests
from bs4 import BeautifulSoup

#Importerer bibliotek av sommersanger og finner ut hvor mange sanger det er på den
songs = pd.read_csv("Sommersanger.csv", encoding ="cp1252")
#print(songs.head())
number_of_songs = list(range(0,(songs.shape[0])))

#Setter antallet sanger skriptet henter ut. Kan endres til manuell input
a = False
while a == False:
    antall = int(input("Hvor mange sanger vil du ha? Svar med et tall mellom 1 og 8: "))
    if antall in range(1,9):
        a = True
    else:
        print("\nPrøv igjen")

#antall = 4

#Det er også mulig å utvikle en variant der brukeren spør om å få en bestemt sang
#Da vil programmet først søke gjennom listen, men hvis sangen ikke finnes der prøver den selv med nettsøk
#Sanger som blir hentet inn slik bør da legges til i tabellen så de kan brukes flere ganger
#Egne ønsker kan kombineres med sanger fra listen

#Overiskt over søkeparametere for hvert sangspråk
settings_dict ={"Norsk": ["sang tekst", "no"],"Svensk": ["sång text", "se"], "Engelsk":["song lyrics", "en"]}

#Løkken velger en og en sang fra listen og spør brukeren om den er godkjent
i=0
while i in range(0, (antall)):

    selected = random.choice(number_of_songs)
    #print(selected)
    song = songs.loc[selected]
    print(f"\n{song[0]}, {song[3]}, {song[4]}")
    approve = str(input("Vil du ha med denne sangen (ja/nei):"))
    if approve == "ja":
    
#Her kan man legge inn valgmuligheter for å filtrere på sjanger og språk
#Drikkeviser, barnesanger og salmer passer ikke alltid sammen.....
#Ser for meg at verktøyet kan brukes til både konfirmasjoner, sommerfester, sommerleir, sommerbryllup, sommerbursdag....
#Noen mennesker jobber som partyfiksere, de trenger det kanskje hver dag. Kantorer kan trenge det hver uke.....

#Denne løkken setter opp søkeparameterne fra listen for valgt sang, basert på språket.
      
        for key, value in settings_dict.items():
            if song[4] in key:
                search_string = str(song[0] +" "+ song[3] +" "+value[0])
                lang = value[1]
            else:
                search_string = song[0] +" "+ song[3] +" "+ settings_dict["Norsk"][0]
                lang = settings_dict["Norsk"][1]

        #print(search_string, lang)
        
#Her kunne man også laget dictionary med ulike søkeparametere basert på sjanger. F.eks. folketoner har ofte ikke
#komponist eller tilhører noen kjent artist. De bør kanskje heller få sjangeren som søkeparameter.
#Drikkeviser har ofte en kjent melodi, og ukjent artist de bør kanskje også ha sjangeren som søkeparameter. 
#Viser har ofte kjent tekstforfatter, mens for pop er det ofte artisten som er mest kjent.
#Det ville også være mulig å legge inn brukerstyring her

#While-løkken er for å gi brukeren lenkevalg om igjen hvis eksport er mislykket:

        b = False
        while b == False:
    
#Dette er selve søket. Det skriver ut flere alternativer det har funnet og lar brukeren velge
            Gsearch = search(search_string, num_results=3, sleep_interval = 5, lang=lang)
            gsearch_list = list(Gsearch)
       
            num=0
            print("\n Hvilken av disse lenkene vil du hente (svar med et tall): ")
            for y in gsearch_list:
                num +=1
                print(num, y)
    
#Her kan man også legge inn mer filtrering av resultater - noen websider er vanskeligere enn andre  
#å parse fra. De kan man la være å vise. Pdf og doc filer er ikke nyttige, evt må ny kode skrives 
#for å kunne hente inn slike filer automatisk. Generator-objektet fra Gsearch var en utfordring å jobbe med.   
            link = int(input("?"))

#Henter websiden, parser html-kodene og finner tekstdelen av den. Henter også rett encoding for å skrive til fil.
#Encoding er tilpasset alfabetet for språkene f.eks. utf-8. Særlig viktig når æøå brukes.
            html = requests.get(gsearch_list[link-1])
            lang_encoding = html.encoding
            soup = BeautifulSoup(html.text, 'html.parser')
            song_text = soup.get_text()

#Skriver ut sangteksten til fil:
            filename = search_string + " " + lang
            text_file = open(filename+".txt", "w", encoding = lang_encoding)
            text_file.write(song_text)
            text_file.close()
        
            print(f"\nSjekk tekstfilen på C:/brukere/dittnavn. Den heter {filename}")
        
#Dette er fortsettelsen på while b==False:

            final_accept = str(input("Aksepterer du filen eller vil du velge igjen fra listen (ja/nei)?"))
            if final_accept == "ja":
                b = True
            else:
                print("Prøv igjen")
        
#Teksten er for lang til å vise på skjermen før printing. Jeg har valgt å la programmet skrive ut sangene individuelt.
#Hvis noen er mislykkede kan man kjøre skriptet flere ganger
#Man kan også tenke seg at gode url'er kan legges til i filen man importerer, så man slipper å søke på nytt hver gang
#man skal bruke samme sang

#En annen mulig utvidelse er å tillate søk etter akkorder eller noter til sangene
        
#Dette er telleren som får den første while-loopen til å gå rundt til man har valgt mange nok sanger
            i+=1
        
#Skriptet kunne ha hatt bedre håndtering av mulige feil, men det vil stort sett bare gi bedre feilmeldinger. 
#De fleste feiltastinger gir nytt forsøk pga bruken av while-loops
