class Domanda:
	def __init__(self, testo : str, opzioni : list, risposta_corretta : int):
		self.testo = testo
		self.opzioni = opzioni
		self.risposta_corretta = risposta_corretta

	def __str__(self):
		ris = f'{self.testo}\n'

		for i in range(len(self.opzioni)):
			ris += f' - {self.opzioni[i]}'
			if i == self.risposta_corretta:
				ris += ' [CORRETTA]\n'
			else:
				ris += '\n'

		return ris

class Quiz:
	def __init__(self, titolo):
		self.titolo = titolo
		self.domande = []
		self.corso = None

	def aggiungiDomanda(self, domanda : Domanda):
		if domanda not in self.domande:
			self.domande.append(domanda)

class Studente:
	def __init__(self, nome : str):
		self.nome = nome
		self.corsi = []

class Corso:
	def __init__(self, titolo : str, descrizione : str, docente : str):
		self.titolo = titolo	
		self.descrizione = descrizione	
		self.docente = docente
		self.quiz = None # 1 - N quiz
		self.studenti = [] # N - N studente

	def aggiungiQuiz(self, quiz : Quiz):
		if self.quiz is None and (quiz.corso is None or quiz.corso == self):
			self.quiz = quiz
			quiz.corso = self

	def aggiungiStudente(self, studente : Studente):
		if studente not in self.studenti:
			self.studenti.append(studente)
		
		if self not in studente.corsi:
			studente.corsi.append(self)

class QuizAttempt:
	def __init__(self, studente : Studente, quiz : Quiz, risposte : list):
		self.studente = studente
		self.quiz = quiz
		self.risposte = risposte
		self.punteggio = self.valutaRisposte()

	def valutaRisposte(self):
		punteggio = 0

		if len(self.quiz.domande) != len(self.risposte):
			return -1

		for i in range(len(self.quiz.domande)):
			if self.risposte[i] == self.quiz.domande[i].risposta_corretta:
				punteggio += 1

		return punteggio
	
	def __str__(self):
		ris = f'Tentativo di {self.studente.nome} per il quiz del {self.quiz.corso.titolo}:\n'
		
		for i in range(len(self.quiz.domande)):
			d = self.quiz.domande[i]
			ris += f'{d.testo} -> {d.opzioni[self.risposte[i]]}'
			if d.risposta_corretta == self.risposte[i]:
				ris += ' [1 punto]\n'
			else:
				ris += ' [0 punti]\n'

		ris += f'Punteggio = {self.punteggio} / {len(self.quiz.domande)}'

		esito = self.punteggio / len(self.quiz.domande)

		if esito < 0.6:
			ris += ' [NON SUPERATO]\n\n'
		else:
			ris += ' [SUPERATO]\n\n'

		return ris

# Esempio di utilizzo
if __name__ == "__main__":
	# Creare un corso
	corso_python = Corso(
		titolo = "Corso Python", 
		descrizione = "Introduzione a Python", 
		docente = "Prof. Rossi")

	# Creare un quiz
	quiz = Quiz("Quiz Python Base")

	# Aggiungere domande al quiz
	domanda1 = Domanda(
		testo = "Cosa è Python?", 
		opzioni = ["Un serpente", "Un linguaggio di programmazione", "Un gioco"],
		risposta_corretta=1)
	
	domanda2 = Domanda(
		testo = "Cosa NON è Python?", 
		opzioni = ["Un linguaggio di programmazione", "Un linguaggio di programmazione", "Un gioco"],
		risposta_corretta=2)
	
	quiz.aggiungiDomanda(domanda1)
	quiz.aggiungiDomanda(domanda2)

	# Impostare il quiz per il corso
	corso_python.aggiungiQuiz(quiz)

	s1 = Studente("Mario")
	s2 = Studente("Luigi")
	s3 = Studente("Pinco")

	corso_python.aggiungiStudente(s1)
	corso_python.aggiungiStudente(s2)
	corso_python.aggiungiStudente(s3)

	# print studenti del corso
	print(f"Studenti del corso {corso_python.titolo}:")
	for studente in corso_python.studenti:
		print(studente.nome)
	print()
	
	# print le domande del quiz
	for domanda in quiz.domande:
		print(domanda)

	quiz_attempt = []

	quiz_attempt.append(QuizAttempt(s1, quiz, [1,1]))
	quiz_attempt.append(QuizAttempt(s2, quiz, [1,2]))
	quiz_attempt.append(QuizAttempt(s1, quiz, [0,0]))

	for qa in quiz_attempt:
		print(qa)
	