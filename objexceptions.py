import time
class SuperUser_name_Error(Exception):
    def __init__(self, name, err_msg):
        super().__init__(err_msg)
        self.name = name
    def __add_users(self):
        pass



class createSuperuserError(SuperUser_name_Error):
    def __init__(self, name, email, message):
        super().__init__(name, message)
        self.email = email
    
    def __add_users(self):
        Add_users = input("enter number of users to add: ")
        try:
            Add_users = int(Add_users)
            for i in range (Add_users):
                user_name =  input(f"Enter user {i + 1} name (With no spaces!) :  ")
                user_email =  input(f"Enter user {i + 1}  email : ")
                try:
                    self.verify_user(user_name, user_email) 
                except createSuperuserError as sp:
                    error_log = open("C:\\Users\\Jack Watua\\Documents\\OPP With Python\\myErrors.txt", "at")
                    if sp.name:
                        error_log.write (f"Name Error: {sp.args[0].format(sp.name)}\n")
                    else:
                        error_log.write (f"Email Error: {sp.args[0].format(sp.email)}\n")
                    error_log.close()
                else:
                    profiles_log = open("C:\\Users\\Jack Watua\\Documents\\OPP With Python\\profiles.txt", "at")
                    profiles_log.write(f"{user_name} Profile created. status - > valid\n")
                    profiles_log.close()

        except ValueError as v:
            print(v.__str__() + " : Invalid number of users!")


    def verify_user(self, username, email):
        if not username.isalpha():
            raise createSuperuserError(username, email, "User name is invalid. Name Cannot include special characters and digits! {}")
        elif "@" not in email:
            raise createSuperuserError(username,email, "Invalid email, check and try again! {}")
        return True


class Demo (createSuperuserError):
    def __init__(self):
        self.name , self.email , self.message = "Jack", "jack@gmail.com", "Invalid trial"
        super().__init__(self.name, self.email, self.message)
    def __add_users(self):
        print("Not allowed to Add Users")
user1 =  createSuperuserError("jacob Watua", "Jack@test.com", "Invalid Entry")

user2 = Demo ()
user2._createSuperuserError__add_users()