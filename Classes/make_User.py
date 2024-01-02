class Users:
    def __init__(self,first_name,last_name,address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.privileges = Privileges()
    def describe_user(self):
        print("Summary of user's profile")
        print(f"- First Name = {self.first_name.title()}\n- Last Name = {self.last_name.title()}\n- Address = {self.address.title()}")
    def greet_user(self):
              print(f"Hello!! {self.first_name.title()} {self.last_name.title()}. Welcome to NEWA TAWA.")
            
              
class Admin(Users):
    def __init__(self,first_name,last_name,address):
        super().__init__(first_name,last_name,address)
        self.privilage = ['can add post','can delete post','can ban user']
    def show_privilage(self):
        print(f"Privilages for {self.first_name.title()} {self.last_name.title()} are:")
        for priv in self.privilage:
            print(priv.title())
            
            
class Privileges:
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']
    def show_privilege(self):
        for priv in self.privileges:
            print(priv.title()) 
    