'''Classifica basata su più condizioni'''

while True:
    n = float(input("Inserisci un numero n: "))
    if n%1 != 0:
        print("Errore. Inserire un numero intero.")
        continue

    if n%2 == 0 and n > 10:
        print("Numero valido")
    else: 
        print("Numero non valido")
    


