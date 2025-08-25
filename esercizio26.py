#Esercizio - 26 Gestione flotta aziendale
#Il programma ci permette di gestire una flotta aziendale di veicoli:
#una azienda ha un insieme di veicoli che vengono utilizzati dai dipendenti per motivi di lavoro. 
#Ogni veicolo ha una marca, un modello e un tipo di carburante (benzina o diesel). 
#Esistono due tipologie di veicoli: auto e camion. 
#Ogni veicolo può essere aggiunto alla flotta, e il programma deve consentire di visualizzare le informazioni sui veicoli.
#Requisiti:
#Creare una classe Veicolo con gli attributi di base: marca, modello e carburante.
#Creare due sottoclassi: Auto e Camion. Ogni sottoclasse deve semplicemente ereditare gli attributi da Veicolo.
#La classe Flotta deve gestire una lista di veicoli, permettere l’aggiunta di nuovi veicoli, e la visualizzazione delle informazioni di tutti i veicoli.
#Crea relativo diagramma UML e codice.

class Veicolo:
    #Qui nel costruttore della classe veicolo aggiungo anche la targa, perchè mi servirà dopo 
    #per verificare se un veicolo è già stato aggiunto alla mia Flotta Aziendale oppure no.
    def __init__(self,targa:str,marca:str ,modello: str,carburante:str):
        self.targa = targa
        self.marca = marca
        self.modello = modello
        self.carburante = carburante

    def __str__(self):
        return f"La targa dell'auto è {self.targa}, la marca è {self.marca}, il modello è {self.modello} e ha questo tipo di carburante {self.carburante}"

class Auto(Veicolo):
    def __init__(self,targa:str,marca:str ,modello: str,carburante:str):
        super().__init__(targa,marca,modello,carburante)
        self.posti = 5

class Camion(Veicolo):
    def __init__(self,targa:str,marca:str ,modello: str,carburante:str):
        super().__init__(targa,marca,modello,carburante)

class Flotta:
    def __init__(self,):
        lista_veicoli = []
