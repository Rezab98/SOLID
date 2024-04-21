# Here is an example of a class that violates the Interface Segregation Principle.

class IUser:
    
    def get_user_info(self):
        pass
    
    def get_user_birthdate(self):
        pass
    
    def get_user_address(self):
        pass
    
    def get_number_of_friends(self):
        pass
    
class Admin(IUser):
    
    def get_user_info(self):
        return "User info"
    
    def get_user_birthdate(self):
        return NotImplementedError("No need for birthdate for admins")
    
    def get_user_address(self):
        return NotImplementedError("No need for address for admins")
    
    def get_number_of_friends(self):
        return NotImplementedError("Admins don't have friends")
    
# The Admin class violates the interface segregation principle because it implements methods that are not needed for an admin user.
# To fix this, we can create a separate interface for admin users:

class IAdminUser:
    
    def get_user_info(self):
        pass

class Admin(IAdminUser):
    
    def get_user_info(self):
        return "User info"
    
    
    