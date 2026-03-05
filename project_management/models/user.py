from models.person import Person

class User(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self._email = email  
        self.projects = []   

    @property
    def email(self):
        return self._email

    def to_dict(self):
        return {"name": self.name, "email": self._email}
