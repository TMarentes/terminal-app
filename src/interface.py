import time

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
        print(f"""
|   THEO'S HUMAN RESOURCES MANAGER
|   Time: {local_hours}:{local_mins} - Date: {local_day}/{local_month}/{local_year}
|   -> Features: https://github.com/TMarentes/terminal-app#features
|   -> Documentation: https://github.com/TMarentes/terminal-app#help-documentation
    
        """)
    
    def menu_interface() -> None:
        print("""
|   HUMAN RESOURCES MENU
|   [1] Search employees
|   [2] Edit employee
|   [3] Add new employee
|   [4] Delete employee
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