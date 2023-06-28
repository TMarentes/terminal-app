class UserInput:
    def __init__ (self):
        pass

    def main_menu_selection():
        selection = int(input("Enter your selection: "))
        if selection in (1,2,3,4):
            return selection
        else:
            raise ValueError
    
    def search_menu_selection():
        selection = int(input("Enter your selection: "))
        if selection in (1,2,3,4):
            return selection
        else:
            raise ValueError
        
    def edit_menu_selection():
        selection = int(input("Enter your selection: "))
        if selection in (1,2,3):
            return selection
        else:
            raise ValueError

    def delete_menu_selection():
        selection = int(input("Enter your selection: "))
        if selection in (1,2,3):
            return selection
        else:
            raise ValueError
    
    def new_employee():
        name = input("Enter a name: ")
        email = input("Enter an email: ")
        department = input("Enter a department: ")
        try:
            salary = int(input("Enter a salary: "))
            return name, email, department, salary
        except ValueError:
            print("Salary must be a number")
        
    
    def export_as_csv():
        selection = input("""

Type 'Yes' to export as csv, enter anything else to skip: """)
        if selection.lower() == "yes":
            return True
        else:
            return False
    
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