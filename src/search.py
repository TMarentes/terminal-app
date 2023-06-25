from user_input import UserInput
from employee import Employee

class Search:
    def __init__ (self):
        pass

    def search_name(name):
        found = False
        for i in range(len(Employee.employees)):
            if name.lower() in Employee.employees[i].name.lower():
                print(f"""
EMPLOYEE DETAILS
Employee Name: {Employee.employees[i].name} 
Employee Email: {Employee.employees[i].email}
Employee Department: {Employee.employees[i].department}
""")
                found = True

        if found == True:
            pass
        else:
            print("Employee not found")

    def search_email(email):
        found = False
        for i in range(len(Employee.employees)):
            if Employee.employees[i].email.lower() == email.lower():
                print(f"""
EMPLOYEE DETAILS
Employee Name: {Employee.employees[i].name} 
Employee Email: {Employee.employees[i].email}
Employee Department: {Employee.employees[i].department}
""")
                found = True

        if found == True:
            pass
        else:
            print("Employee not found")
