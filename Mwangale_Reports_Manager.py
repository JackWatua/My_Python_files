#Create a report manager bot

'''CREATE CUSTOM EXCEPTIONS CLASS TO HANDLE USER DEFINED ERROR/ CUSTOM ERRORS (Reports Errors, Permission Errors)'''
#MUST HAVE 6 :Report ERROR functions
#report name errors, report details errror, report permision errors(detele/ edit errors), unexisiting report errors, blank reports errors
#update error logs of necessary 
#MUST HAVE 7 : Permission Error functions





from email import message
from email.message import Message


class PermisionError (Exception):
    pass

class ReportError (Exception):
    def __init__(self,message = "**{}** must include _hr ot _ac or _gen"):
        super().__init__(message)
        self.message = message
        







'''CREATE A CLASS (REPORTS EXTENDS REPORT_ERRORS)'''
#MUST HAVE 1 : Allows user to create a new report 
#MUST HAVE 2 : Categorizes the roports into different categories.
#MUST Have 3 : Reports must capture date and time crated, edited or deleted 
#Must HAVE 4 : Generates reports based on user  



class reports(ReportError):
    report_title = ""
    category = ""
    date_created = ""
    date_edited = ""
    date_deleted = ""
    created_by = ""
    report_file = ""
    def __init__(self):
        super().__init__()


    def create_report(self, title, category, creator, date):
        self.report_title = title
        self.category = category
        self.created_by = creator
        self.date_created = date
        if self.report_title.endswith("_hr"):
            self.report_file = open(f"C:\\Users\\Jack Watua\\Documents\\OPP With Python\\Mwangale Reports\\HR files\\{self.report_title}.txt", "w")
        elif self.report_title.endswith("_ac"):
            self.report_file = open(f"C:\\Users\\Jack Watua\\Documents\\OPP With Python\\Mwangale Reports\\Finances Files\\{self.report_title}.txt", "w")
        else:
            self.report_file = open(f"C:\\Users\\Jack Watua\\Documents\\OPP With Python\\Mwangale Reports\\General Files\\{self.report_title}.txt", "w")
        self.report_file.close()
        return f"New report created\nDetails\nTitle: {self.report_title}\nCreated by : {self.created_by}\nDate : {self.date_created}"


    







'''Create a class (permisions) EXTENDS PERMISION ERRORS'''
#Set different user permissions. SuperUser and nornal user capabilities. eg only admins can delete or edit a report once it is submitted etc..



class permisions(PermisionError):
    pass











'''CREATE A REPORT USERS EXTENDS REPORTS, PERMISIONS'''
#MUST HAVE 5 USER DETAILS (user name, email, role, department)
#MUST HAVE 6 : Include report editing / updating and deleting functions.

class User(reports, permisions):
    user_name = ""
    email = ""
    department = ""
    role = ""
    def __init__(self, name, email):
        super().__init__()
        self.user_name = name
        self.email = email
    
    def set_details(self, department, role):
        self.department = department
        self.role = role

    def create_report(self, title):
        self.title = title
        try:
            assert self.validate_title() 
            assert self.check_name()
        except ReportError as r:
            if r.message:
                return(r)
            else:
                return f"{r.args[0].format(self.title)}"
        else:
            return super().create_report(self.title, self.department, self.user_name, date = "Today")
    def validate_title(self):
        if not self.title.endswith("_hr"):
            if  not self.title.endswith("_ac"):
                if not self.title.endswith("_gen"):
                    raise ReportError()
        return True

    def check_name(self, message= "Title already exists!"):
        self.message = message
        if self.title in ["Week14_ac", "Week14_hr", "Week14_gen"]:
            raise ReportError(message = message)
        return True



'''
user1 = User("Jacob Watua", "jack@test.com")
user1.department = "Accounting"
print(user1.create_report("Week14_js"))
'''

user2 = User("Danstan Michael Wasobokha Wanyonyi", "DanstanWasobokhwa01@gmail.com")
user2.department = "Accounting"

print(user2.create_report("Wasobokha_ac"))