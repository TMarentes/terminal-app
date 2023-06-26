from user_input import UserInput

class Employee:
    employees = []
    def __init__ (self, name, email, department, salary):
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary
        Employee.employees.append(self)

    def edit_employee_by_name(name):
        input_name = UserInput.update_by_name()
        input_email = UserInput.update_by_email()
        input_department = UserInput.update_by_department()
        input_salary = UserInput.update_by_salary()
        found = False
        for i in range(len(Employee.employees)):
            if Employee.employees[i].name.lower() == name.lower():
                Employee.employees[i].name = input_name
                Employee.employees[i].email = input_email
                Employee.employees[i].department = input_department
                Employee.employees[i].salary = input_salary
                found = True

        if found == True:
            print("Employee updated")
        else:
            print("Employee not found")



    def edit_employee_by_email(self, email):
        input_name = UserInput.update_by_name()
        input_email = UserInput.update_by_email()
        input_department = UserInput.update_by_department()
        input_salary = UserInput.update_by_salary()
        found = False
        for i in range(len(Employee.employees)):
            if Employee.employees[i].email.lower() == email.lower():
                Employee.employees[i].name = input_name
                Employee.employees[i].email = input_email
                Employee.employees[i].department = input_department
                Employee.employees[i].salary = input_salary
                found = True

        if found == True:
            print("Employee updated")
        else:
            print("Employee not found")


    def new_employee(name, email, department, salary):
        Employee(name, email, department, salary)
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