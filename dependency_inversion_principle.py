# This simple example violates the dependency inversion principle.

class DbConnection:
    def connect(self):
        return "Database connection"
    
class User:
    def __init__(self, db_connection: DbConnection):
        self.db_connection = db_connection
        
    def get_user_info(self):
        return "User info"
    
    def save_user(self):
        connection = self.db_connection.connect()
        # Save user to database
    
# The User class violates the dependency inversion principle because it depends on a concrete implementation of the DbConnection class.
# To fix this, we can create an interface for the DbConnection class:

class IDbConnection:
    def connect(self):
        pass
    
class DbConnection(IDbConnection):
    def connect(self):
        return "Database connection"
    
class User:
    def __init__(self, db_connection: IDbConnection):
        self.db_connection = db_connection
        
    def get_user_info(self):
        return "User info"
    
    def save_user(self):
        connection = self.db_connection.connect()
        # Save user to database
        

# Now if we want to change the database connection implementation, we can create a new class that implements the IDbConnection interface
