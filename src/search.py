from user_input import UserInput
from employee import Employee

class Search:
    def __init__ (self):
        pass

    def search_name(name):
        found = False
        for i in range(len(Employee.employees)):
            if name.lower() in Employee.employees[i].name.lower():
                print(f"""Name: {Employee.employees[i].name}, Email: {Employee.employees[i].email}, Department: {Employee.employees[i].department}, Salary: {Employee.employees[i].salary}""")
                found = True

        if found == True:
            pass
        else:
            print("Employee not found")

    def search_email(email):
        found = False
        for i in range(len(Employee.employees)):
            if email.lower() in Employee.employees[i].email.lower():
                print(f"""Name: {Employee.employees[i].name}, Email: {Employee.employees[i].email}, Department: {Employee.employees[i].department}, Salary: {Employee.employees[i].salary}""")
                found = True

        if found == True:
            pass
        else:
            print("Employee not found")
