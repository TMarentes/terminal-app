from employee import Employee

import pytest

Employee("Michael Scott", "michael.scott@gmail.com", "manager", 105000)
Employee("Pam Beesly", "pam.beesly@gmail.com", "assistant", 62000)


class TestEmployee:

    def test_delete_by_name_valid(self) -> None:
        result = Employee.delete_employee_by_name("Pam Beesly")
        assert result == True

    def test_delete_by_name_invalid(self) -> None:
        result = Employee.delete_employee_by_name("John Lennon")
        assert result == False

    def test_entering_new_salary(self) -> None:
        user_input = "String"
        result = ""
        try:
            input_salary = int(user_input)
        except ValueError:
            result = "Salary must be a number."
        assert result == "Salary must be a number."

    def new_employee(self) -> None:
        input = ("Jon Samson", "j.samson@gmail.com", "marketing", 29000)
        result = Employee.new_employee(input)
        assert result == "Employee added"
