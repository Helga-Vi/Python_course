Final Exercise Noroff Accelerate Python
Katarina Jørgensen 23.06.2023

Sangheftegenerator

Dette prosjektet ble til fordi jeg lager konsertprogrammer til koret mitt. Det er litt for spesielt for oppgaven,
men prinsippene ligner. Profesjonelle partyfiksere kan trenge dette hver dag, kantorer hver uke. Kjekt å ha hvis
man har en syngende og festglad vennekrets eller familie, eller bare har litt dårlig fantasi før en konfirmasjon
eller sommerleir. 

Jeg har laget en sangheftegenerator for sommersanger. Regnearket "sommersanger.xlsx" inneholder et bredt utvalg av sanger med 
sommertema på ulike språk og i ulike sjangere (28 stykker). Programmet spør bruker om hvor mange sanger han/hun trenger og plukker et 
tilfeldig utvalg at sanger fra listen. Bruker har selv mulighet til å takke ja eller nei til valgene.(Jeg har ikke lagt inn brukerstyrt
forhåndsfiltrering av sangene før tilfeldig valg, men det er også en mulighet)

Programmet leter på internett etter teksten til godkjente sanger. Den søker på originalspråket til sangen og bruker en søkestreng
med nøkkelord på riktig språk. Programmet henter inn ca. 3 topptreff fra google og bruker kan selv velge hvilken lenke programmet
prøver å hente tekst fra. Noen treff kan være helt feil, noen sangtekstsider gir mye ekstratekst sammen med sangen. Dette må brukeren
lære selv for å få den store fleksibiliteten som programmet gir. (Utbedring av søkestrengene og filtrering av treffene 
kan også gi bedre søkeresultater, men uansett ikke perfekte resultater)

Programmet henter deretter hovedteksten fra valgt nettside og eksporterer denne til tekstfil. Det er da som oftest en smal sak for bruker
å markere selve sangteksten og hente den inn i f.eks. Adobe InDesign eller Word for å lage et proft utseende sanghefte av flere tekster.
For at det ikke ska bli for mye å forholde seg til for bruker så henter programmet en enkelt sang til hver tekstfil som lages. 
Bruker får også muligheten til å si nei til filen og velge en ny link for å hente teksten, dersom den første var feil eller full av
overflødig tekst. Dersom man kjører programmet om igjen får man jo et nytt tilfeldig valg.

Det er mange muligheter for utvidelse av funksjonaliteten til programmet - disse er skissert i selve koden, på den plassen hvor de evt 
ville ha stått. 