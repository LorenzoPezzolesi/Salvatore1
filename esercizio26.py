class Veicolo:
    #Qui nel costruttore della classe veicolo aggiungo anche la targa, perchè mi servirà dopo 
    #per verificare se un veicolo è già stato aggiunto alla mia Flotta Aziendale oppure no.
    def __init__(self, targa:str, marca:str , modello: str, carburante:str):
        self.targa = targa
        self.marca = marca
        self.modello = modello
        self.carburante = carburante

    def __str__(self):
        return f"La targa dell'auto è {self.targa}, la marca è {self.marca}, il modello è {self.modello} e ha questo tipo di carburante {self.carburante}"

class Auto(Veicolo):
    def __init__(self, targa:str, marca:str , modello: str, carburante:str, posti:int):
        super().__init__(targa,marca,modello,carburante)
        self.posti = posti

    def __str__(self):
        return f"{super().__str__()} - {self.posti} posti"

class Camion(Veicolo):
    def __init__(self,targa:str,marca:str ,modello: str,carburante:str,portata:float):
        super().__init__(targa,marca,modello,carburante)
        self.portata = portata

    def __str__(self):
        return f"{super().__str__()} - {self.portata} Kg"

class Flotta:
    def __init__(self,):
        self.veicoli: list[Veicolo]= []

    def aggiungi_veicolo(self, veicolo:Veicolo):
        for v in self.veicoli:
            if v.targa == veicolo.targa:
                return False
        self.veicoli.append(veicolo)
        return True

    def visualizza_flotta(self):
        for veicolo in self.veicoli:
            print(veicolo.__str__())

    def restituisci_flotta(self):
        return self.veicoli
class Dipendente:
    def __init__(self, nome: str, cognome: str, codice_fiscale: str):
        self._nome = nome
        self._cognome = cognome
        self._cf = codice_fiscale

#Esempio di utilizzo:
if __name__ == "__main__":
    flotta = Flotta()
    auto = Auto("AB123CD", "Fiat", "Panda", "benzina",5)
    camion = Camion("XY456ZW", "Iveco", "Daily", "diesel", 3500)
    dipendente = Dipendente("Mario", "Rossi", "RSSMRA80A01H501A")

    # stampa esito aggiunta veicolo
    if flotta.aggiungi_veicolo(auto):
        print("Auto aggiunta alla flotta")
    else:
        print("Auto già presente nella flotta")

    if flotta.aggiungi_veicolo(auto):
        print("Auto aggiunta alla flotta")
    else:
        print("Auto già presente nella flotta")

    if flotta.aggiungi_veicolo(camion):
        print("Camion aggiunto alla flotta")
    else:
        print("Camion già presente nella flotta")
    
    print("\nLista veicoli:")
    veicoli = flotta.restituisci_flotta()
    for v in veicoli:
        print(v.__str__())