from user_input import UserInput
from employee import Employee


class Search:
    def __init__(self):
        pass

    def search_name(name) -> list:
        found = False
        employee = []
        for i in range(len(Employee.employees)):

            if name.lower() in Employee.employees[i].name.lower():
                employee.append([Employee.employees[i].name, Employee.employees[i].email,
                                Employee.employees[i].department, Employee.employees[i].salary])
                print(
                    f"""Name: {Employee.employees[i].name}, Email: {Employee.employees[i].email}, Department: {Employee.employees[i].department}, Salary: {Employee.employees[i].salary}""")
                found = True

        if found:
            return employee
        else:
            print("Employee not found")
            return employee

    def search_email(email) -> list:
        found = False
        employee = []
        for i in range(len(Employee.employees)):
            if email.lower() in Employee.employees[i].email.lower():
                employee.append([Employee.employees[i].name, Employee.employees[i].email,
                                Employee.employees[i].department, Employee.employees[i].salary])
                print(
                    f"""Name: {Employee.employees[i].name}, Email: {Employee.employees[i].email}, Department: {Employee.employees[i].department}, Salary: {Employee.employees[i].salary}""")
                found = True

        if found:
            return employee
        else:
            print("Employee not found")
            return employee

    def list_all() -> list:
        print("NAME, EMAIL, DEPARTMENT, SALARY")
        employee_list = []
        for i in range(len(Employee.employees)):
            line = ""
            line = Employee.employees[i].name+", "+Employee.employees[i].email+", " + \
                Employee.employees[i].department+", " + \
                str(Employee.employees[i].salary)
            employee_list.append([Employee.employees[i].name, Employee.employees[i].email,
                                 Employee.employees[i].department, str(Employee.employees[i].salary)])
            print(line)
        return employee_list
