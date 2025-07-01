from persona import Persona

class Professore(Persona):
    def __init__(self, nome:str, cognome:str, età:int, facoltà:str, ore_lezione:int):
        super().__init__(nome, cognome, età)
        self.facoltà = facoltà
        self.ore_lezione = ore_lezione 
    
    def __str__(self):
        return super().__str__()+f"Insegna presso la facoltà di: {self.facoltà}\nLe sue ore di lezione settimanali sono: {self.ore_lezione}"
    

    def __call__(self):
        super().__call__()
        if self.ore_lezione <= 5:
            print(f"{self.nome} {self.cognome} è un assistente.")
        elif 5 < self.ore_lezione <= 25:
            print(f"{self.nome} {self.cognome} lavora part-time.")
        else:
            print(f"{self.nome} {self.cognome} lavora full-time.")


professore = Professore(nome="Nicoletta", cognome="Giorgi", età=50, facoltà="Lettere moderne", ore_lezione=15)
print(professore)
professore()

professore2 = Professore("Filippo", "Sordi", 33, "Storia", 60)
print(professore2)
professore2()





class Professore(Persona):
 
    def __init__(self, nome, cognome, eta, facoltà, ore_lezione):
 
        if eta < 25:
            raise ValueError("Un professore deve avere almeno 25 anni")
        super().__init__(nome, cognome, eta)
 
        if ore_lezione < 0:
            raise ValueError("Errore: le ore di lezione non possono essere negative")
        self.facoltà = facoltà.title()
        self.ore_lezione = ore_lezione

    def __str__(self):
        return super().__str__() + f"\nInsegna preso la facoltà: {self.facoltà}\nOre di lezione settimanale: {self.ore_lezione}"
    
    def __call__(self):
        # print(super().__call__()) # stampa da Persona
 
        if self.ore_lezione <= 5:
            print(f"{self.getNome()} {self.getCognome()} è un assistente") 
        elif 5 < self.ore_lezione < 20:
            print(f"{self.getNome()} {self.getCognome()} lavora part time")
        else:
            print(f"{self.getNome()} {self.getCognome()} lavora full time")

 
# istanza della classe Professore
if __name__ == "__main__":
    try:
        prof = Professore(nome="Francisco", cognome="Soto", eta=26, facoltà="Lettere Moderne", ore_lezione=19)
        print(prof)
        prof()
    except ValueError as e:
        print(f"Errore: {e}")