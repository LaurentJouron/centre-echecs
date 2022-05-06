class GlobalApp:

    @staticmethod
    def start_app():
        welcome = " Welcome to the << CHESS-CENTER >> application "
        print(f"\n{welcome.center(106, ' ')}")
        instruction = " Please follow the instructions below "
        print(f"\n{instruction.center(106, ' ')}")

    @staticmethod
    def reception():
        reception_name = " RECEPTION "
        print(f"\n{reception_name.center(106, '~')}")

    @staticmethod
    def choice():
        choice = " Make your choice "
        print(f"{choice.center(106, '*')}")

    @staticmethod
    def start_menu():
        to_do = "> [1]Player list  [2]Tournament  [3]Match  [4]Quit <"
        print(f"\n{to_do.center(106, '-')}")

    @staticmethod
    def input():
        choice = input(f"Please enter an order : ").capitalize()
        choice = int(choice)
        return choice
