# This simple example violates the Liskov substitution principle.

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def get_user_info(self):
        return f"User: {self.name}, email: {self.email}"
    
    def work(self):
        return "I am working"

class VIPUser(User):
    def __init__(self, name: str, email: str, phone: str):
        super().__init__(name, email)
        self.phone = phone

    def get_user_info(self):
        return f"VIP User: {self.name}, email: {self.email}, phone: {self.phone}"
    
    def work(self):
        return NotImplementedError("VIP users don't work")
    
# The VIPUser class violates the Liskov substitution principle because the work method in the VIPUser class raises an error.
    
