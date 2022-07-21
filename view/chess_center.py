

class ChessCenterView:

    @staticmethod
    def welcome_application():
        welcome_application = " Welcome to the << CHESS-CENTER >> application "
        print(f"\n{welcome_application.center(106, ' ')}")

    @staticmethod
    def instruction():
        instruction = " Please follow the instructions below "
        print(f"\n{instruction.center(106, ' ')}")

    @staticmethod
    def reception_name():
        reception_name = " RECEPTION "
        print(f"\n{reception_name.center(106, ' ')}")

    @staticmethod
    def choice_decoration():
        choice_decoration = " Make your choice "
        print(f"{choice_decoration.center(106, '*')}")

    @staticmethod
    def start_menu():
        start_menu = "> [1]Player list  [2]Tournament  [3]Round  [4]Quit <"
        print(f"\n{start_menu.center(106, '-')}")

    @staticmethod
    def input_menu():
        return input("Select the menu number : ")

    @staticmethod
    def value_error():
        print("Value error.")

    @staticmethod
    def exit_program():
        exit_programme = " EXIT CHESS CENTER "
        print(f"\n{exit_programme.center(106, ' ')}")

    @staticmethod
    def exiting_program():
        information_decoration = " Exiting the program "
        print(f"{information_decoration.center(106, '*')}")

    @staticmethod
    def exit_confirmation_menu():
        exit_list = "> [1]Non  [2]Yes <"
        print(f"\n{exit_list.center(106, '-')}")
