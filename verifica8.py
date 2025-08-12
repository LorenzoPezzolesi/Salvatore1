from enum import Enum
from datetime import date
from typing import List

class TipoMiele(Enum):
	ACACIA = "ACACIA"
	TIGLIO = "TIGLIO"
	CASTAGNO = "CASTAGNO"
	MILLEFIORI = "MILLEFIORI"
	EUCALIPTO = "EUCALIPTO"
	ALTRO = "ALTRO"

class Apicoltore:
	def __init__(self, id_apicoltore : str, nome : str, numero_licenza : str):
		self.id_apicoltore = id_apicoltore
		self.nome = nome
		self.numero_licenza = numero_licenza
		self.alveari : List[Alveare] = []

	def produzione_per_tipo(self):
		ris = {}

		# t = ACACIA | TIGLIO | CASTAGNO ...
		for t in TipoMiele:
			tot = 0
			# tutti gli alverari
			for a in self.alveari:
				# ogni raccolta dell'alveare
				for r in a.raccolte:
					# se ho raccolto del miele del tipo t -> sommo peso
					if r.tipo == t:
						tot += r.quantita_kg
			
			ris[t] = tot

		return ris

	def alveare_piu_produttivo(self) -> "Alveare":
		ris : "Alveare" = None
		produzione = -1

		for a in self.alveari:
			if a.produzione_totale() > produzione:
				produzione = a.produzione_totale()
				ris = a

		return ris

	def registra_raccolta(self, alveare : "Alveare", quantita_kg : float, tipo : TipoMiele, note : str = None) -> "RaccoltaMiele":
		ris = RaccoltaMiele("r1", date.today(), quantita_kg, tipo, note)

		if alveare not in self.alveari:
			self.alveari.append(alveare)

		alveare.aggiungi_raccolta(ris)

		return ris


	def aggiungi_alveare(self, alveare : "Alveare") -> None:
		if alveare not in self.alveari:
			self.alveari.append(alveare)

class Sciame:
	def __init__(self, id_sciame : str, numero_api_stimato : int, ha_regina : bool):
		self.id_sciame = id_sciame
		self.numero_api_stimato = numero_api_stimato
		self.ha_regina = ha_regina

class Alveare:
	def __init__(self, id_alveare : str, posizione_gps : str, data_installazione : date, sciame : Sciame):
		self.id_alveare = id_alveare
		self.posizione_gps = posizione_gps
		self.data_installazione = data_installazione
		self.sciame = sciame
		self.raccolte : List[RaccoltaMiele] = []

	def produzione_totale(self) -> float :
		ris = 0

		for r in self.raccolte:
			ris += r.quantita_kg

		return ris
	
	def media_raccolte(self) -> float :
		if len(self.raccolte) > 0:
			return self.produzione_totale() / len(self.raccolte)
		else:
			return 0	
	
	def aggiungi_raccolta(self, raccolta : "RaccoltaMiele") -> None:
		if raccolta not in self.raccolte:
			self.raccolte.append(raccolta)
	
	def eta_giorni(self) -> int:
		return (date.today() - self.data_installazione).days

class RaccoltaMiele:
	def __init__(self, idRaccolta : str, data_raccolta : date, quantita_kg : float, tipo : TipoMiele, note : str):
		self.idRaccolta = idRaccolta
		self.data_raccolta = data_raccolta
		self.quantita_kg = quantita_kg
		self.tipo = tipo
		self.note = note

def main() -> None:
	# Creazione di un apicoltore
	apicoltore = Apicoltore(id_apicoltore="AP001", nome="Giuseppe Miele", numero_licenza="LIC2024001")

	# Creazione di sciami
	sciame1 = Sciame(id_sciame="S001", numero_api_stimato=50000, ha_regina=True)
	sciame2 = Sciame(id_sciame="S002", numero_api_stimato=45000, ha_regina=True)
	sciame3 = Sciame(id_sciame="S003", numero_api_stimato=30000, ha_regina=False)

	# Creazione di alveari
	alveare1 = Alveare(
		id_alveare="ALV001", posizione_gps="45.464664, 9.188540", data_installazione=date(2024, 3, 15), sciame=sciame1
	)
	alveare2 = Alveare(
		id_alveare="ALV002", posizione_gps="45.465123, 9.189876", data_installazione=date(2024, 4, 10), sciame=sciame2
	)
	alveare3 = Alveare(
		id_alveare="ALV003", posizione_gps="45.463987, 9.187234", data_installazione=date(2024, 2, 20), sciame=sciame3
	)

	# Aggiunta degli alveari all'apicoltore
	apicoltore.aggiungi_alveare(alveare1)
	apicoltore.aggiungi_alveare(alveare2)
	apicoltore.aggiungi_alveare(alveare3)

	# Registrazione di raccolte
	apicoltore.registra_raccolta(
		alveare=alveare1, quantita_kg=25.5, tipo=TipoMiele.ACACIA, note="Ottima qualità, colore chiaro"
	)
	apicoltore.registra_raccolta(alveare=alveare1, quantita_kg=18.3, tipo=TipoMiele.TIGLIO, note="Aroma intenso")
	apicoltore.registra_raccolta(
		alveare=alveare2, quantita_kg=22.0, tipo=TipoMiele.MILLEFIORI, note="Mix di fiori di campo"
	)
	apicoltore.registra_raccolta(
		alveare=alveare2, quantita_kg=15.7, tipo=TipoMiele.CASTAGNO, note="Colore scuro, sapore forte"
	)

	# Visualizzazione dei risultati
	print(f"\nApicoltore: {apicoltore.nome}")
	print(f"Licenza: {apicoltore.numero_licenza}")
	print(f"Numero alveari: {len(apicoltore.alveari)}")

	print("\nProduzione per tipo di miele:")
	produzione = apicoltore.produzione_per_tipo()
	for tipo, quantita in produzione.items():
		if quantita > 0:
			print(f"  {tipo.value}: {quantita:.1f} kg")

	alveare_top = apicoltore.alveare_piu_produttivo()
	if alveare_top:
		print(f"\nAlveare più produttivo: {alveare_top.id_alveare} ({alveare_top.produzione_totale():.1f} kg)")

	print("\nDettagli alveari:")
	for alveare in apicoltore.alveari:
		print(f"\n  {alveare.id_alveare}:")
		print(f"    Posizione: {alveare.posizione_gps}")
		print(f"    Regina presente: {'Sì' if alveare.sciame.ha_regina else 'No'}")
		print(f"    API stimate: {alveare.sciame.numero_api_stimato:,}")
		print(f"    Produzione totale: {alveare.produzione_totale():.1f} kg")
		print(f"    Media per raccolta: {alveare.media_raccolte():.1f} kg")
		print(f"    Età alveare: {alveare.eta_giorni()} giorni")


if __name__ == "__main__":
	main()