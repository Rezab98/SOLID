#This simple example violates the open/closed principle.

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def get_user_info(self):
        return f"User: {self.name}, email: {self.email}"
    
class UserSaver:
    def save_user(self, format: str, user: User):
        if format == "txt":
            with open("users.txt", "a") as file:
                file.write(f"{user.name}, {user.email}\n")
        elif format == "json":
            with open("users.json", "a") as file:
                file.write(f"{{name: {user.name}, email: {user.email}}}\n")
                
            
# The UserSaver class is not closed for modification because if we want to save user information in a different format,
# we need to modify the UserSaver class to add a new if statement.
# To fix this, we need to make the UserSaver class open for extension and closed for modification:

class UserSaver:
    def save_user(self, user: User):
        pass
    
class TxtSaver(UserSaver):
    def save_user(self, user: User):
        with open("users.txt", "a") as file:
            file.write(f"{user.name}, {user.email}\n")

class JsonSaver(UserSaver):
    def save_user(self, user: User):
        with open("users.json", "a") as file:
            file.write(f"{{name: {user.name}, email: {user.email}}}\n")



