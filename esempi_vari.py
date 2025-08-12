# commento 
# creo una variabile

# nome_variabile = valore
class Persona:
	# le cose che caratterizzano una Persona
	def __init__(self, nome: str, cognome: str, citta: str, eta : int):
		'''
		*nome*: Nome della persona\n
		*cognome*: Cognome della persona\n
		*citta*: Città di nascita della persona\n
		'''
		self._nome = nome
		self._cognome = cognome
		self._citta = citta
		self._eta = eta
		self.volte_saluti = 0

	@property
	def citta(self):
		return self._citta

	@citta.setter
	def citta(self, citta):
		if citta == "NO":
			self._citta = ""
		else:
			self._citta = citta

	def set_eta(self, eta):
		if eta < 0:
			print("Errore")
		elif eta >= 0 and eta <= 9:
			print("Bambino")
		elif eta >= 10 and eta <= 13:
			print("Ragazzino 1")
		elif eta >= 14 and eta <= 17:
			print("Ragazzino 2")
		else:
			print("Adulto")


class Studente(Persona):
	def __init__(self, nome, cognome, citta, eta, classe):
		super().__init__(nome, cognome, citta, eta)
		self._classe = classe

p = Persona("Alex", "Lenzi", "PI", 24)
print(f'\t{p.citta}')
p.__citta = "ciao"
print(f'{" "*25} {p.citta}')

print('*' * 50)

somma = 0

# for i in range(5):
# 	n = int(input("Inserisci un numero: "))
# 	somma = somma + n
# 
# print(f'Somma = {somma}')

# ***************************************************

somma = 0
count = 0

n = int(input('Inserisci un numero: '))
while n != 0:
	somma = somma + n
	count = count + 1
	n = int(input('Inserisci un numero: '))

print(f'Somma = {somma}')
if count > 0:
	print(f'Media = {somma / count}')
else:
	print('Non hai inserito valori!')

