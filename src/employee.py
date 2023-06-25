from user_input import UserInput

class Employee:
    employees = []
    def __init__ (self, name, email, department):
        self.name = name
        self.email = email
        self.department = department
        Employee.employees.append(self)

    def edit_employee_by_name(name):
        input = UserInput.edit_by_name()
        input = input.split(',')
        input_name = input[0]
        input_email = input[1]
        input_department = input[2]
        found = False
        index = 0
        for i in range(len(Employee.employees)):
            if Employee.employees[i].name.lower() == name.lower():
                Employee.employees[i].name = input_name
                Employee.employees[i].email = input_email
                Employee.employees[i].department = input_department
                found = True

        if found == True:
            print("Employee updated")
        else:
            print("Employee not found")



    def edit_employee_by_email(self, email):
        input = UserInput.edit_by_email()
        input = input.split(',')
        input_name = input[0]
        input_email = input[1]
        input_department = input[2]
        found = False
        index = 0
        for i in range(len(Employee.employees)):
            if Employee.employees[i].email.lower() == email.lower():
                Employee.employees[i].name = input_name
                Employee.employees[i].email = input_email
                Employee.employees[i].department = input_department
                found = True

        if found == True:
            print("Employee updated")
        else:
            print("Employee not found")


    def new_employee(name, email, department):
        Employee(name, email, department)
        print("New employee," ,name, ", was added")

    def delete_employee_by_name(name):
        found = False
        for i in range(len(Employee.employees)):
            if Employee.employees[i].name.lower() == name.lower():
                del Employee.employees[i]
                found = True

        if found == True:
            print("Employee deleted")
        else:
            print("Employee not found")

    def delete_employee_by_email(email):
        found = False
        for i in range(len(Employee.employees)):
            if Employee.employees[i].email.lower() == email.lower():
                del Employee.employees[i]
                found = True

        if found == True:
            print("Employee deleted")
        else:
            print("Employee not found")