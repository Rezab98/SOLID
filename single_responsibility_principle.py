# This simple example violates the single responsibility principle.

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def get_user_info(self):
        return f"User: {self.name}, email: {self.email}"

    def save_user(self):
        with open("users.txt", "a") as file:
            file.write(f"{self.name}, {self.email}\n")

# It violates the single responsibility principle because the User class is responsible for two things: 
# getting user information and saving user information.
# To fix this, we can create a separate class for saving user information:

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def get_user_info(self):
        return f"User: {self.name}, email: {self.email}"
    
class UserSaver:    
    def save_user(self, user: User):
        with open("users.txt", "a") as file:
            file.write(f"{user.name}, {user.email}\n")
