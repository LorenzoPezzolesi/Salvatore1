from datetime import datetime

class Utente:
	def __init__(self, nome_utente, email, password, profilo):
		self.nome_utente = nome_utente
		self.email = email
		self.password = password
		self.profilo = profilo
		self.follower = 0
		self.foto = []
		self.album = []

	# creazione del profilo
	def crea_profilo(self, profilo):
		self.profilo = profilo

	# aggiungi foto alla lista di Foto
	def carica_foto(self, foto):
		self.foto.append(foto)

	def segui(self, utente):
		utente.follower += 1

	def aggiungi_album(self, album):
		if album not in self.album:
			self.album.append(album)

class Foto:
	def __init__(self, id, titolo, descrizione, utente, album):
		self.id = id
		self.titolo = titolo
		self.descrizione = descrizione
		self.data_caricamento = datetime.now()
		self.utente = utente
		self.album = album
		self.commenti = []

	def commenta(self, commento):
		if commento not in self.commenti:
			self.commenti.append(commento)
			return True
		else:
			return False

	def __str__(self):
		return f'{self.id} - titolo : {self.titolo} ({self.descrizione}) caricato il {self.data_caricamento}'

class Album:
	def __init__(self, titolo, descrizione, utente):
		self.titolo = titolo
		self.descrizione = descrizione
		self.utente = utente
		self.foto = []

	# dice True se NON era presente | False altrimenti
	def aggiungi_foto(self, foto) -> bool: 
		if foto not in self.foto:
			self.foto.append(foto)
			return True
		else:
			return False
	
	# dice True se era presente | False altrimenti
	def rimuovi_foto(self, foto) -> bool:
		return self.foto.pop(foto) != None

class Commento:
	def __init__(self, utente, commento, foto):
		self.utente = utente
		self.commento = commento
		self.foto = foto


utente = Utente("alex", "alex@..", "pwd", "AMM")
print(utente.profilo)
utente.crea_profilo("ciao")
print(utente.profilo)

foto = Foto(1, "Titolo", "Desc", None, None)
print(foto)