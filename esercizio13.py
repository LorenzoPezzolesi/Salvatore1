class Stanza:
	def __init__(self, nome : str, superficie : int):
		self.nome = nome
		self.superficie = superficie
		self.casa = None

class Casa:
	def __init__(self, indirizzo : str, proprietario : str):
		self.indirizzo = indirizzo
		self.proprietario = proprietario
		self.stanze = [] 
	
	def aggiungi_stanza(self, stanza : Stanza):
		if stanza not in self.stanze and (stanza.casa is None or stanza.casa == self):
			self.stanze.append(stanza)
			stanza.casa = self
			return True
		else:
			return False
		


# Creazione dell'istanza di Casa
casa = Casa("Via delle Rose 15", "Maria Rossi")
casa2 = Casa("Via delle Rose 16", "Luigi Verdi")

# Creazione delle istanze di Stanza
soggiorno = Stanza("Soggiorno", 30)
cucina = Stanza("Cucina", 15)
camera = Stanza("Camera da Letto", 20)

# Aggiunta delle stanze alla casa
casa.aggiungi_stanza(soggiorno)
casa.aggiungi_stanza(cucina)
casa.aggiungi_stanza(camera)

casa2.aggiungi_stanza(soggiorno)

# Verifica dell'associazione
print(f"Casa di {casa.proprietario} situata in {casa.indirizzo} contiene le seguenti stanze:")
for stanza in casa.stanze:
	print(f"- {stanza.nome} ({stanza.superficie} mq)")

# Verifica dell'associazione
print(f"Casa di {casa2.proprietario} situata in {casa2.indirizzo} contiene le seguenti stanze:")
for stanza in casa2.stanze:
	print(f"- {stanza.nome} ({stanza.superficie} mq)")