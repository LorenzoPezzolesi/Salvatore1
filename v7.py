from datetime import datetime, date
from typing import Dict, List
from enum import Enum

class CategoriaSpesa(Enum):
	CIBO = "Cibo"
	TRASPORTI = "Trasporti"
	CASA = "Casa"
	SVAGO = "Svago"
	SALUTE = "Salute"
	ALTRO = "Altro"

class TipologiaTransazione(Enum):
	ENTRATA = "Entrata"
	USCITA = "Uscita"

class Utente:
	def __init__(self, id_utente: str, nome_utente: str, email: str):
		self.id_utente = id_utente
		self.nome_utente = nome_utente
		self.email = email
		self.conti: List[ContoBancario] = []

	def registra_transazione(self, conto: "ContoBancario", importo: float, categoria: CategoriaSpesa, descrizione: str) -> None:
		transazione = Transazione(importo, descrizione, conto, categoria)
		conto.aggiungi_transazione(transazione)

	def totale_spese_mensili(self) -> float:
		totale = 0.0

		for conto in self.conti:
			spese_mensili_conto = conto.report_mensile()
			for t in spese_mensili_conto:
				totale += t.importo

		return totale
	
	def spese_per_categoria(self) -> Dict[CategoriaSpesa, float]:
		spese : Dict[CategoriaSpesa, float] = {}

		# Creo una cosa del tipo
		# {CIBO: 0.0, TRASPORTI: 0.0, CASA: 0.0, SVAGO: 0.0, SALUTE: 0.0, ALTRO: 0.0}
		for cs in CategoriaSpesa:
			spese[cs] = 0.0

		for conto in self.conti:
			for t in conto.transazioni:
				if t.tipologia == TipologiaTransazione.USCITA:
					spese[t.categoria] += t.importo

		# Avremo una cosa del tipo
		# {CIBO: 50.0, TRASPORTI: 30.0, CASA: 0.0, SVAGO: 200.0, SALUTE: 0.0, ALTRO: 0.0}
		return spese
	
	def categoria_piu_costosa(self) -> CategoriaSpesa:
		spese = self.spese_per_categoria()

		spesa_massima = None
		importo_massimo = 0.0

		for categoria in spese:
			importo = spese[categoria]
			if importo > importo_massimo:
				importo_massimo = importo
				spesa_massima = categoria

		return spesa_massima

class ContoBancario:
	def __init__(self, id_conto : str, nome_conto : str, saldo_iniziale : float):
		self.id_conto = id_conto
		self.nome_conto = nome_conto
		self.saldo_attuale = saldo_iniziale
		self.saldo_iniziale = saldo_iniziale
		self.transazioni: List[Transazione] = []

	def aggiungi_transazione(self, transazione: "Transazione") -> None:
		self.transazioni.append(transazione)
		if transazione.tipologia == TipologiaTransazione.USCITA:
			self.saldo_attuale -= transazione.importo
		else:
			self.saldo_attuale += transazione.importo

	def saldo_disponibile(self) -> float:
		return self.saldo_attuale
	
	def media_spese_totali(self) -> float:
		somma_spese = 0.0
		numero_spese = 0

		for transazione in self.transazioni:
			if transazione.tipologia == TipologiaTransazione.USCITA:
				somma_spese += transazione.importo
				numero_spese += 1

		if numero_spese == 0:
			return 0.0

		return somma_spese / numero_spese

	def report_mensile(self):
		mese = date.today().month
		anno = date.today().year

		spese : List[Transazione] = []

		for t in self.transazioni:
			if t.data.month == mese and t.data.year == anno and t.tipologia == TipologiaTransazione.USCITA:
				spese.append(t)

		return spese

class Transazione:
	__id = 1

	def __init__(self, importo: float, descrizione: str, conto : ContoBancario, categoria: CategoriaSpesa):
		self.id = f"T{Transazione.__id}"
		Transazione.__id += 1
		self.data = datetime.now()
		self.descrizione = descrizione
		if importo > 0:
			self.importo = importo
			self.tipologia = TipologiaTransazione.ENTRATA
		else:
			self.importo = importo * -1
			self.tipologia = TipologiaTransazione.USCITA
		self.conto = conto
		self.categoria = categoria

def main() -> None:
	# Creazione di un utente
	utente: Utente = Utente(id_utente="U1", nome_utente="Mario Rossi", email="mario.rossi@email.com")

	# Creazione di due conti bancari
	conto_principale: ContoBancario = ContoBancario(id_conto="C1", nome_conto="Conto Principale", saldo_iniziale=1000.0)
	conto_risparmi: ContoBancario = ContoBancario(id_conto="C2", nome_conto="Conto Risparmi", saldo_iniziale=5000.0)

	# Aggiunta dei conti all'utente
	utente.conti.extend([conto_principale, conto_risparmi])

	# Registrazione di alcune transazioni
	utente.registra_transazione(
		conto=conto_principale, importo=-50.0, categoria=CategoriaSpesa.CIBO, descrizione="Spesa settimanale"
	)

	utente.registra_transazione(
		conto=conto_principale, importo=-30.0, categoria=CategoriaSpesa.TRASPORTI, descrizione="Benzina"
	)

	utente.registra_transazione(
		conto=conto_principale, importo=1000.0, categoria=CategoriaSpesa.ALTRO, descrizione="Stipendio"
	)

	utente.registra_transazione(
		conto=conto_risparmi, importo=-200.0, categoria=CategoriaSpesa.SVAGO, descrizione="Weekend fuori città"
	)

	# Visualizzazione dei risultati
	print(f"\nUtente: {utente.nome_utente}")
	print(f"Email: {utente.email}")

	for conto in utente.conti:
		print(f"\nConto: {conto.nome_conto}")
		print(f"Saldo disponibile: €{conto.saldo_disponibile():.2f}")
		print(f"Media spese totali: €{conto.media_spese_totali():.2f}")

	print("\nStatistiche spese:")
	spese: Dict[CategoriaSpesa, float] = utente.spese_per_categoria()
	for categoria, importo in spese.items():
		if importo > 0:
			print(f"{categoria.value}: €{importo:.2f}")

	categoria_max: CategoriaSpesa = utente.categoria_piu_costosa()
	print(f"\nCategoria più costosa: {categoria_max.value}")
	print(f"Totale spese mensili: €{utente.totale_spese_mensili():.2f}")


if __name__ == "__main__":
	main()