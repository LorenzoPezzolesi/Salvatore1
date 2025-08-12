class Corso:
	def __init__(self, titolo : str, codice : str):
		self.titolo = titolo
		self.codice = codice
		self.studenti = []

class Studente:
	def __init__(self, nome : str, matricola : str):
		self.nome = nome
		self.matricola = matricola
		self.corsi = []

	def aggiungi_corso(self, corso : Corso):
		if corso not in self.corsi:
			self.corsi.append(corso)
		
		if self not in corso.studenti:
			corso.studenti.append(self)


# Creazione delle istanze di Studente
studente1 = Studente("Alice Rossi", "MAT123")
studente2 = Studente("Marco Bianchi", "MAT456")

# Creazione delle istanze di Corso
corso1 = Corso("Programmazione Python", "PY101")
corso2 = Corso("Database Relazionali", "DB201")
corso3 = Corso("Sistemi Operativi", "SO301")

# Associazione tra studenti e corsi
studente1.aggiungi_corso(corso1)
studente1.aggiungi_corso(corso1)
studente1.aggiungi_corso(corso1)
studente1.aggiungi_corso(corso1)
studente1.aggiungi_corso(corso1)
studente1.aggiungi_corso(corso2)
studente2.aggiungi_corso(corso2)
studente2.aggiungi_corso(corso3)

# Verifica delle associazioni
print(f"{studente1.nome} è iscritto ai seguenti corsi:")
for corso in studente1.corsi:
	print(f"- {corso.titolo} ({corso.codice})")

print(f"\n{corso2.titolo} ha i seguenti studenti iscritti:")
for studente in corso2.studenti:
	print(f"- {studente.nome} ({studente.matricola})")