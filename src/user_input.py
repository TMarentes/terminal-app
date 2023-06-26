class UserInput:
    def __init__ (self):
        pass

    def menu_selection():
        return int(input("Enter your selection: "))
    
    def new_employee():
        name = input("Enter a name: ")
        email = input("Enter an email: ")
        department = input("Enter a department: ")
        salary = input("Enter a salary: ")
        return name, email, department, salary
    
    def enter_to_continue():
        input("Press enter to continue...")

    def search_by_name():
        return input("Enter a name: ")

    def search_by_email():
        return input("Enter an email: ")

    def search_by_department():
        return input("Enter a department: ")
    

    def update_by_name():
        return input("Enter a new name: ")

    def update_by_email():
        return input("Enter a new email: ")

    def update_by_department():
        return input("Enter a new department: ")
    
    def update_by_salary():
        return input("Enter a new salary: ")