from terminal import Terminal 
from user_input import UserInput
from interface import Interface
from search import Search
from employee import Employee

Employee("John Garrison", "john.g@gmail.com", "marketing")
Employee("John Garrison2", "john.g@gmail.com", "marketing")

if __name__ == "__main__":

    Interface.start_interface()
    UserInput.enter_to_continue() 

    while True:
        Terminal.clear_terminal()
        Interface.menu_interface()

        try:
            option = UserInput.menu_selection()
        except ValueError:
            print("Closing application")
            break

        match option:
            case 1:
                Terminal.clear_terminal()
                Interface.search_interface()
                try:
                    option2 = UserInput.menu_selection()
                    Terminal.clear_terminal()
                except ValueError:
                    print("Closing application")
                    break

                match option2:
                    case 1:
                        search_results = Search.search_name(UserInput.search_by_name())
                        # EXPORT AS CSV ?
                        UserInput.enter_to_continue() 
                    case 2:
                        search_results = Search.search_email(UserInput.search_by_email())
                        UserInput.enter_to_continue() 
                    case 3:
                        pass

            case 2:
                Terminal.clear_terminal()
                Interface.edit_interface()
                try:
                    option3 = UserInput.menu_selection()
                    Terminal.clear_terminal()
                except ValueError:
                    print("Closing application")
                    break
                
                match option3:
                    case 1:
                        Employee.edit_employee_by_name(UserInput.search_by_name())
                        UserInput.enter_to_continue() 

                    case 2:
                        Employee.edit_employee_by_email(UserInput.search_by_email())
                        UserInput.enter_to_continue() 

                    case 3:
                        pass

                
            case 3:
                Terminal.clear_terminal()
                input = UserInput.new_employee()
                Employee.new_employee(input[0], input[1], input[2])
                UserInput.enter_to_continue() 
            
            case 4:
                Terminal.clear_terminal()
                Interface.delete_interface()
                try:
                    option4 = UserInput.menu_selection()
                    Terminal.clear_terminal()
                except ValueError:
                    print("Closing application")
                    break

                match option4:
                    case 1:
                        Employee.delete_employee_by_name(UserInput.search_by_name())
                        UserInput.enter_to_continue() 

                    case 2:
                        Employee.delete_employee_by_email(UserInput.search_by_email())
                        UserInput.enter_to_continue() 
                        

                    case 3:
                        pass







