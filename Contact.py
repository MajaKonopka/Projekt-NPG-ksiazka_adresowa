import uuid
class Contact:
    def __init__(self,name,surname,phoneNumber):
        """
            Inicjalizuje nową instancję klasy Contact z podanym imieniem, nazwiskiem i numerem telefonu.
            Automatycznie generowany jest unikalny identyfikator UUID.

            Parametry:
            name (str): Imię kontaktu.
            surname (str): Nazwisko kontaktu.
            phoneNumber (str): Numer telefonu kontaktu.
        """
        self.name = name
        self.surname = surname
        self.phoneNumber = phoneNumber
        self.uuid = str(uuid.uuid4())