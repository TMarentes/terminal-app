from employee import Employee
from search import Search
import pytest

Employee("Michael Scott", "michael.scott@gmail.com", "manager", 105000)
Employee("Pam Beesly", "pam.beesly@gmail.com", "assistant", 62000)

class TestSearch:

    def test_search_by_name(self) -> None:
        result = Search.search_name("Michael")
        assert result[0] == ["Michael Scott", "michael.scott@gmail.com", "manager", 105000]

        result = Search.search_name("Pam")
        assert result[0] == ["Pam Beesly", "pam.beesly@gmail.com", "assistant", 62000]

        result = Search.search_name("Theo Marentes")
        assert result == []
    
    def test_search_by_email(self) -> None:
        result = Search.search_email("michael.scott@gmail.com")
        assert result[0] == ["Michael Scott", "michael.scott@gmail.com", "manager", 105000]

        result = Search.search_email("pam.beesly@gmail.com")
        assert result[0] == ["Pam Beesly", "pam.beesly@gmail.com", "assistant", 62000]

        result = Search.search_email("theo.marentes@gmail.com")
        assert result == []

    def test_list_all(self) -> None:
        result = Search.list_all()
        assert result[0][1] == "michael.scott@gmail.com"

    