import math

print("Questo programma calcola il perimetro di tre figure geometriche")


scelta = input("Scegli tra 'quadrato' 'cerchio' 'rettangolo': ")

if scelta == "quadrato":
        lato= float(input("Inserisci la lunghezza del lato: "))
        perimetro = 4 * lato
        print("Il perimetro del quadrato è", perimetro)

elif scelta == "cerchio":
        raggio = float(input("Inserisci la lunghezza del raggio: "))
        circonferenza = raggio * math.pi * 2
        print("La circonferenza del cerchio è", circonferenza)

elif scelta == "rettangolo":
        base= float(input("Inserisci la lunghezza della base: "))
        altezza= float(input("Inserisci la lunghezza dell'altezza: "))
        perimetro= 2 * base + 2 * altezza
        print("Il perimetro del rettangolo è", perimetro)

else:
         print("Risposta non valida")

input("premi un tasto per uscire dal programma..")

