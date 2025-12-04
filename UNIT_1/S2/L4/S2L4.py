import math

print("scegli una figura geometrica per calcolarne il perimetro\n 1 quadrato\n 2 cerchio\n 3 rettangolo ")


number = input("inserisci il numero di una figura: ")
if number == "1":
    lato = float(input("inserisci la lugnhezza del lato: "))
    print("il perimetro del lato è: ", 4 * lato)
elif number == "2":
    raggio = float(input("inserisci la lunghezza del raggio: "))
    print("la circonferenza del cerchio è: ", 2 * math.pi * raggio)
elif number == "3":
    altezza = float(input("inserisci la lunghezza dell'altezza: "))
    base = float (input("inserisci la lunghezza della base: "))
    print("il perimetro del rettangolo è: ", 2*altezza + 2*base)

else:
    print("il valore che hai inserito non è corretto!!!")