class Motore:
	def __init__(self, numero_seriale : str, tipo : str):
		self.numero_seriale = numero_seriale
		self.tipo = tipo
		self.auto = None #

class Auto:
	def __init__(self, marca : str, modello : str):
		self.marca = marca
		self.modello = modello
		self.motore = None #

	def associa_motore(self, motore : Motore):
		# se non ho un motore E ( motore non ha auto O motore assegnato a questa auto - self )
		if self.motore is None and (motore.auto is None or motore.auto == self):
			self.motore = motore
			motore.auto = self #

# Creazione delle istanze
auto1 = Auto("Fiat", "500")
motore1 = Motore("ENG123456", "Benzina")

# Associazione tra auto e motore
auto1.associa_motore(motore1)

# Verifica dell'associazione
print(f"{auto1.marca} {auto1.modello} ha il motore: {auto1.motore.numero_seriale}")
print(f"Il motore {motore1.numero_seriale} appartiene a: {motore1.auto.marca} {motore1.auto.modello}")