'''Si scriva una funzione ricorsiva charDuplicator che consenta di duplicare ogni carattere in una stringa e restituisca il risultato sotto forma di una nuova stringa.

Ad esempio, se la stringa "libro" viene data in input a charDuplicator, la funzione ricorsiva deve produrre in output la stringa "lliibbrroo".'''

def charDuplicator(my_string:str) -> str:
    if not my_string:
        return ""
    else:
        return my_string[0] * 2 + charDuplicator(my_string[1:])

print(charDuplicator("libro"))
print(charDuplicator("Arcobaleno"))



def charDuplicator(my_string:str) -> str:
    if my_string == "":
        return ""
    else:
        return my_string[0] * 4 + (charDuplicator(my_string[1:]))

print(charDuplicator("letto"))
    


def charDuplicator(stringa1:str) -> str:
    if stringa1 == "":
        return ""
    else:
        return stringa1[0] * 2 + (charDuplicator(stringa1[1:]))