from user_input import UserInput
from interface import Interface
from logic import Logic
from terminal import Terminal


if __name__ == "__main__":
    Terminal.clear_terminal()
    Interface.start_interface()
    UserInput.enter_to_continue()
    Logic.run_logic()
