import time
from request import Requests
from employee import Employee


class Interface:
    def __init__(self):
        pass

    def start_interface() -> None:
        local = time.localtime()
        local_hours = local.tm_hour
        local_mins = local.tm_min
        local_year = local.tm_year
        local_month = local.tm_mon
        local_day = local.tm_mday
        quote = Requests.get_quote()
        quote_length = len(quote[0]["quote"])
        selected_quote = ""
        for i in range(0, 20):  # sets request limit to 20
            if quote_length >= 70:
                quote = Requests.get_quote()
                quote_length = len(quote[0]["quote"])
            else:
                selected_quote = quote[0]["quote"]
                break

        print(f"""
|   THEO'S HUMAN RESOURCES MANAGER
|   Time: {local_hours}:{local_mins} - Date: {local_day}/{local_month}/{local_year}
|
|   -> Features: https://github.com/TMarentes/terminal-app#features
|   -> Documentation: https://github.com/TMarentes/terminal-app#help-documentation
| 
|   "{selected_quote}"
|   - {quote[0]["author"]}
    
        """)

    def menu_interface() -> None:
        total_employees = len(Employee.employees)
        print(f"""
|   HUMAN RESOURCES MENU
|   Total Employees: {total_employees}
|   [1] Search employees
|   [2] Edit employees
|   [3] Add new employees
|   [4] Delete employees
|   [Enter anything else to exit]
        """)

    def search_interface() -> None:
        print("""
|   EMPLOYEE SEARCH OPTIONS
|   [1] Search by name
|   [2] Search by email
|   [3] List all employees
|   [4] Go back
|   [Enter anything else to exit]
        """)

    def edit_interface() -> None:
        print("""
|   EMPLOYEE EDIT OPTIONS
|   [1] Find by name
|   [2] Find by email
|   [3] Go back
|   [Enter anything else to exit]
        """)

    def delete_interface() -> None:
        print("""
|   EMPLOYEE DELETE OPTIONS
|   [1] Delete by name
|   [2] Delete by email
|   [3] Go back
|   [Enter anything else to exit]
        """)

    def add_interface() -> None:
        print("""
|   EMPLOYEE ADD OPTIONS
|   [1] Add new employee
|   [2] Import "The Office UK" employees
|   [3] Import "The Office US" employees
|   [4] Go back
|   [Enter anything else to exit]
        """)
