import bcrypt
from .Enums import Admin_Type, Admin_Permissions

#------------   Simple Admin definition  ----------------------------
class Admin:
    def __init__(self, username, password, admin_type):
        self.username = username #string
        self._password_hash = self.hash_password(password)
        self.admin_type = admin_type #enum
        self._password_reset_required = True
    
    #username
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, name):
        if not isinstance(name, str):
            raise TypeError("username must be a string")
        self.__username = name

    #password
    def hash_password(self, password):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode(), salt)
    
    def check_password(self, input_password):
        return bcrypt.checkpw(input_password.encode(), self._password_hash)
    
    def set_new_password(self, new_password):
        self._password_hash = self.hash_password(new_password)
        self._password_reset_required = False
    


    #admin type
    @property
    def admin_type(self):
        return self.__admin_type
    @admin_type.setter
    def admin_type(self, admin_type):
        if not isinstance(admin_type, Admin_Type):
            raise TypeError("admin type must be Admin_Type enum")
        self.__admin_type = admin_type
    
    #permissions
    @property
    def permissions(self):
        return set()
        


##### ------------------- level 1 , God of Destruction 
class Admin_GoD(Admin):
    @property
    def permissions(self):
        return {Admin_Permissions.EDIT_GUIDE}
    
    
##### --------------------- level 2 , Angel
class Admin_Angel(Admin_GoD):
    @property
    def permissions(self): #add char, equipment, or assign guide 
        return super().permissions | {Admin_Permissions.ADD_ASSET, Admin_Permissions.EDIT_ASSET, Admin_Permissions.ASSIGN_GUIDE}
    
    

##### --------------------  level 3 , Supreme Kai
class Admin_Supreme_Kai(Admin_Angel):
    @property
    def permissions(self): #create admin or promote admin
        return super().permissions | {Admin_Permissions.DELETE_ASSET, Admin_Permissions.EDIT_ADMIN}
    


##### --------------------  level 4 , Zeno
class Admin_Zeno(Admin_Supreme_Kai): 
    @property
    def permissions(self): #delete admin
        return super().permissions | {Admin_Permissions.DELETE_ADMIN}



