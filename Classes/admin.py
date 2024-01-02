from user_module import Users

class Admin(Users):
    def __init__(self,first_name,last_name,address):
        super().__init__(first_name,last_name,address)
        self.privilage = ['can add post','can delete post','can ban user']
    def show_privilage(self):
        print(f"Privilages for {self.first_name.title()} {self.last_name.title()} are:")
        for priv in self.privilage:
            print(priv.title())