#add training status
#add salary
#add list all users
#add export as csv
#handle errors
#constraints, salary must be a number check


from terminal import Terminal 
from user_input import UserInput
from interface import Interface
from search import Search
from employee import Employee

Employee("Michael Scott", "michael.scott@gmail.com", "manager", 105000)
Employee("Pam Beesly", "pam.beesly@gmail.com", "assistant", 62000)
Employee("Jim Halpert", "jim.halpert@gmail.com", "sales", 86000)
Employee("Dwight Schrute", "dwight.schrute@gmail.com", "sales", 87000)
Employee("Angela Martin", "angela.martin@gmail.com", "accounting", 72000)
Employee("Meredith Palmer", "angela.martin@gmail.com", "relations", 74000)

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
                        Search.list_all()
                        UserInput.enter_to_continue()
                    case 4:
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







