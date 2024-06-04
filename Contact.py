import uuid
class Contact:
    def __init__(self,name,surname,phoneNumber):
        self.name = name
        self.surname = surname
        self.phoneNumber = phoneNumber
        self.uuid = str(uuid.uuid4())