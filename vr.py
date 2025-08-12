from datetime import datetime
from typing import List

class ElementoMenu:
	def __init__(self, codice: str, nome: str, prezzo: float, tempo_preparazione: int, allergeni: List[str], disponibile: bool):
		self._codice = codice
		self._nome = nome
		self._prezzo = prezzo
		self._tempo_preparazione = tempo_preparazione
		self._allergeni = allergeni
		self._disponibile = disponibile

	def get_codice(self):
		return self._codice
	
	def get_nome(self):
		return self._nome
	
	def get_prezzo(self):
		return self._prezzo
	
	def get_tempo_preparazione(self):
		return self._tempo_preparazione
	
	def get_allergeni(self):
		return self._allergeni
	
	def is_disponibile(self):
		return self._disponibile
	
	def set_disponibile(self, stato : bool):
		self._disponibile = stato

	def to_string(self):
		return f'{self._codice} {self._nome} ({self._prezzo} €) pronto in {self._tempo_preparazione} minuti'

class PrimoPiatto(ElementoMenu):
	def __init__(self, codice: str, nome: str, prezzo: float, tempo_preparazione: int, allergeni: List[str], disponibile: bool):
		super().__init__(codice, nome, prezzo, tempo_preparazione, allergeni, disponibile)
		self._tipo_pasta = ''
		self._vegetariano = False

	def get_tipo_pasta(self):
		return self._tipo_pasta
	
	def is_vegetariano(self):
		return self._vegetariano
	
	def set_tipo_pasta(self, tipo : str):
		self._tipo_pasta = tipo
		
	def set_vegetariano(self, vegetariano : bool):
		self._vegetariano = vegetariano

class SecondoPiatto(ElementoMenu):
	def __init__(self, codice: str, nome: str, prezzo: float, tempo_preparazione: int, allergeni: List[str], disponibile: bool):
		super().__init__(codice, nome, prezzo, tempo_preparazione, allergeni, disponibile)
		self._cottura_default = ''

	def get_cottura_default(self):
		return self._cottura_default
	
	def set_cottura_default(self, cottura : str):
		self._cottura_default = cottura

	def to_string(self):
		return f'{super().to_string()} cottura {self._cottura_default}'

class Ordine:
	def __init__(self, numero_ordine: str, data_ora: datetime, stato: str, elementi: List[ElementoMenu]):
		self._numero_ordine = numero_ordine
		self._data_ora = data_ora
		self.set_stato(stato)
		self._elementi = elementi

	def get_numero_ordine(self):
		return self._numero_ordine
	
	def get_data_ora(self):
		return self._data_ora

	def get_stato(self):
		return self._stato

	def set_stato(self, stato : str):
		if stato.lower() in ["in_attesa", "in_preparazione", "pronto", "servito"]:
			self._stato = stato.lower()
		else:
			self._stato = "in_attesa"

	def aggiungi_elemento(self, elemento : ElementoMenu):
		if elemento not in self._elementi:
			self._elementi.append(elemento)

	def rimuovi_elemento(self, elemento : ElementoMenu):
		self._elementi.remove(elemento)

	def calcola_totale(self):
		totale = 0

		for elemento in self._elementi:
			totale += elemento.get_prezzo()

		return totale

class Tavolo:
	def __init__(self, numero: int, posti: int, stato: str):
		self._numero = numero
		self._posti = posti
		self.set_stato(stato)
		self._ordini : List[Ordine] = []

	def get_numero(self):
		return self._numero

	def get_posti(self):
		return self._posti

	def is_libero(self):
		return self._stato == "libero"

	def set_stato(self, stato : str):
		if stato in ["libero", "occupato"]:
			self._stato = stato
		else:
			self._stato = "libero"

	def aggiungi_ordine(self, ordine : Ordine):
		if ordine not in self._ordini:
			self._ordini.append(ordine)

	def get_ordini_attivi(self):
		ris = []

		for ordine in self._ordini:
			if ordine.get_stato() not in ["pronto", "servito"]:
				ris.append(ordine)

		return ris

def main():
	# Creazione elementi del menu
	primo = PrimoPiatto("P1", "Spaghetti Carbonara", 12.0, 15, ["uova", "glutine"], True)
	primo.set_tipo_pasta("spaghetti")
	primo.set_vegetariano(False)

	secondo = SecondoPiatto("S1", "Bistecca", 18.0, 20, [], True)
	secondo.set_cottura_default("media")

	# Creazione tavolo e ordine
	tavolo = Tavolo(1, 4, "libero")
	ordine = Ordine("ORD1", datetime.now(), "in_attesa", [])

	# Aggiunta elementi all'ordine
	ordine.aggiungi_elemento(primo)
	ordine.aggiungi_elemento(secondo)

	# Associazione ordine al tavolo
	tavolo.aggiungi_ordine(ordine)
	tavolo.set_stato("occupato")

	# Calcoli
	print(f"Totale ordine: {ordine.calcola_totale()}€")  # Output: Totale ordine: 30.0€

	# Gestione stato ordine
	ordine.set_stato("in_preparazione")
	print(f"Stato ordine: {ordine.get_stato()}")  # Output: Stato ordine: in_preparazione

	# Informazioni tavolo
	print(f"Tavolo numero: {tavolo.get_numero()}")
	print(f"Stato tavolo: {'libero' if tavolo.is_libero() else 'occupato'}")
	print(f"Ordini attivi: {len(tavolo.get_ordini_attivi())}")

	print(primo.to_string())
	print(secondo.to_string())

if __name__ == '__main__':
	main()
