from datetime import date
class User:
    def __init__(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        firstName = db.String(64), index=True) 
        

    def getFirstName(self):
        return self.firstName

    def setFirstName(self,firstName: str):
        self.firstName = firstName
    
    def getLastName(self):
        return self.lastName

    def setLastName(self, lastName: str):
        self.lastName = lastName

    def getPassword(self):
        return self.password
    
    def setPassword(self, password: str):
        self.password = password

    def getAdress(self):
        return self.adress

    def setAdress(self,adress: str):
        self.adress = adress
    
    def getEmail(self):
        return self.email

    def setEmail(self, email: str):
        self.email = email
    
    def getCreationDate(self):
        return self.creationDate.strftime("%d/%m/%Y")

    def setCreationDate(self, dates):
        self.getCreationDate = date