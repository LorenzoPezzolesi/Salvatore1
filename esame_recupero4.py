class Utente:
    def __init__(self, user_id: str, nome: str, email: str):
        self.user_id = user_id
        self.nome = nome
        self.email = email

class Lezione:
    def __init__(self, titolo: str, durata_minuti: int):
        self.titolo = titolo
        self.durata_minuti = durata_minuti

class Corso:
    def __init__(
        self,
        codice_corso: str,
        titolo: str,
        docente: "Docente",
        lezioni: list[Lezione] ,
        studenti_iscritti: list['Studente'] ,
    ):
        self.codice_corso = codice_corso
        self.titolo = titolo
        self.docente = docente
        self.lezioni = lezioni
        self.studenti_iscritti = studenti_iscritti

    def aggiungi_studente(self, studente: 'Studente') -> bool:
        for s in self.studenti_iscritti:
            if s.user_id == studente.user_id:
                return False
        self.studenti_iscritti.append(studente)
        return True
    
    def get_numero_iscritti(self) -> int:
        return len(self.studenti_iscritti)
#              ^ ^
#              | |
#              | |
#Con len(): restituisce un numero intero che rappresenta la quantità di studenti

class Docente(Utente):
    def __init__(self, user_id: str, nome: str, email: str, corsi_insegnati: list[Corso] = None):
        super().__init__(user_id, nome, email)
        self.corsi_insegnati = corsi_insegnati

    def crea_lezione(self, corso: Corso, titolo_lezione: str, durata: int) -> Lezione:
        lezione = Lezione(titolo_lezione, durata)
        corso.lezioni.append(lezione)
        return lezione

class Studente(Utente):
    def __init__(self, user_id: str, nome: str, email: str, corsi_iscritti: list[Corso] = None):
        super().__init__(user_id, nome, email)
        self.corsi_iscritti = corsi_iscritti 
    
    def iscriviti_corso(self, corso: Corso) -> bool:
        successo = corso.aggiungi_studente(self)
        if successo:
            self.corsi_iscritti.append(corso)
            print(successo)
            return True
        else:
            print(successo)
            return False

#Il Main ha degli errori
def main():
    # 1. Creazione di un docente e due studenti
    docente_rossi = Docente("DOC01", "Prof. Mario Rossi", "m.rossi@scuola.it")
    studente_bianchi = Studente("STU01", "Luca Bianchi", "l.bianchi@email.it")
    studente_verdi = Studente("STU02", "Giulia Verdi", "g.verdi@email.it")

    # 2. Creazione di un corso, assegnato al docente
    corso_python = Corso("PY101", "Programmazione con Python", docente_rossi)
    # Aggiungiamo il corso alla lista dei corsi del docente
    docente_rossi.corsi_insegnati.append(corso_python)
    print(f"Corso '{corso_python.titolo}' creato e assegnato al {docente_rossi.nome}.")

    # 3. Il docente crea due lezioni per il suo corso
    lezione1 = docente_rossi.crea_lezione(corso_python, "Introduzione a Python", 45)
    lezione2 = docente_rossi.crea_lezione(corso_python, "Variabili e Tipi di Dati", 60)
    print(f"Aggiunte {len(corso_python.lezioni)} lezioni al corso.")

    # 4. Iscrizione degli studenti al corso
    studente_bianchi.iscriviti_corso(corso_python)
    studente_verdi.iscriviti_corso(corso_python)

    # 5. Tentativo di iscrivere di nuovo uno studente (per testare la logica)
    studente_bianchi.iscriviti_corso(corso_python)

    # 6. Stampa di un report finale
    print("\n--- REPORT FINALE CORSO ---")
    print(f"Corso: {corso_python.titolo} [{corso_python.codice_corso}]")
    print(f"Docente: {corso_python.docente.nome}")
    print(f"Numero di iscritti: {corso_python.get_numero_iscritti()}")
    print("Elenco studenti iscritti:")
    for studente in corso_python.studenti_iscritti:
        print(f"- {studente.nome} ({studente.email})")
    print("--------------------------")
    # Output Atteso:
    #
    # Corso 'Programmazione con Python' creato e assegnato al Prof. Mario Rossi.
    # Aggiunte 2 lezioni al corso.
    # True
    # True
    # False
    #
    # --- REPORT FINALE CORSO ---
    # Corso: Programmazione con Python [PY101]
    # Docente: Prof. Mario Rossi
    # Numero di iscritti: 2
    # Elenco studenti iscritti:
    # - Luca Bianchi (l.bianchi@email.it)
    # - Giulia Verdi (g.verdi@email.it)
    # --------------------------

if __name__ == "__main__":
    main()