'''Scrivere un programma che acquisisca una stringa inserita dall'utente e generi una nuova stringa che 
corrisponda alla versione invertita della stringa originale. Il programma deve poi visualizzare la stringa 
ottenuta in output. Per risolvere il problema non si deve utilizzare alcun tipo di funzione, ma esclusivamente
 i cicli.'''

valore: str = input("Inserisci una stringa: ")
new_stringa = ""
for i in range(len(valore)- 1, -1, -1):
    new_stringa += valore[i]
print(new_stringa)
