class Corso:
	def __init__(self, nome: str, durata: str):
		self.nome = nome
		self.durata = durata
		self.studenti = []

	def __str__(self):
		return f'{self.nome} ({self.durata})'

class Insegnante:
	def __init__(self, nome : str, cognome : str, strumento : str):
		self.nome = nome
		self.cognome = cognome
		self.strumento = strumento
		self.studenti = []

	def __str__(self):
		return f'{self.cognome} {self.nome} [{self.strumento}]'

class Studente:
	def __init__(self, nome : str, cognome : str):
		self.nome = nome
		self.cognome = cognome
		self.insegnante = None
		self.corsi = []

	def iscrivi_corso(self, corso: Corso):
		if corso not in self.corsi:
			self.corsi.append(corso)
		
		if self not in corso.studenti:
			corso.studenti.append(self)

	def set_insegnante(self, insegnante: Insegnante):
		if self.insegnante is None:
			self.insegnante = insegnante

			# aggiungo me stesso (studente - self) se non sono 
			# già uno studente dell'insegnante
			if self not in insegnante.studenti:
				insegnante.studenti.append(self)

	# sovrascrive la stampa di un oggetto standard (<__main__.nome_classe object at indirizzo_memoria>)
	def __str__(self):
		ris = f'Studente {self.cognome} {self.nome} con insegnante {self.insegnante}.\n'
		ris += 'Corsi:\n'
		for corso in self.corsi:
			ris += f'- {corso}\n'
		return ris

def main():
	# Creazione degli insegnanti
	insegnante1 = Insegnante('Mario', 'Rossi', 'Pianoforte')
	insegnante2 = Insegnante('Luca', 'Bianchi', 'Chitarra')

	# Creazione degli studenti
	studente1 = Studente('Anna', 'Verdi')
	studente2 = Studente('Marco', 'Neri')

	# Assegnazione degli insegnanti agli studenti
	studente1.set_insegnante(insegnante1)
	studente2.set_insegnante(insegnante2)

	# Creazione dei corsi
	corso1 = Corso('Teoria Musicale', '3 mesi')
	corso2 = Corso('Tecnica Pianistica', '6 mesi')

	# Iscrizione degli studenti ai corsi
	studente1.iscrivi_corso(corso1)
	studente1.iscrivi_corso(corso2)
	studente2.iscrivi_corso(corso1)

	# Stampa delle informazioni
	print(studente1)
	print(studente2)

if __name__ == '__main__':
	main()