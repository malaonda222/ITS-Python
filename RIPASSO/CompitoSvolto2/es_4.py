'''Scrivi una funzione che prenda in input una lista di dizionari 
che rappresentano voti di studenti e aggrega i voti per studente 
in un nuovo dizionario.'''

def aggrega_voti(voti: list[dict]) -> dict[str, list[int]]:
    new_dict = {}
    for item in voti:
        nome = item["nome"]
        voto = item["voto"]
        if nome not in new_dict:
            new_dict[nome] = []
        new_dict[nome].append[voto]
    return new_dict


