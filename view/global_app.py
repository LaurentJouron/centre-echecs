class GlobalApp:

    @staticmethod
    def start_app():
        """Reception to the start application.
        Print:
            str: welcome and instruction """
        welcome = " Welcome to the << CHESS-CENTER >> application "
        print(f"\n{welcome.center(106, ' ')}")
        instruction = " Please follow the instructions below "
        print(f"\n{instruction.center(106, ' ')}")

    @staticmethod
    def reception():
        """Title in reception to the start application.
        Print:
            str: reception_name """
        reception_name = " RECEPTION "
        print(f"\n{reception_name.center(106, '~')}")

    @staticmethod
    def choice():
        """Explains that you must choose between several options.
        Print:
            str: * choice * """
        choice = " Make your choice "
        print(f"{choice.center(106, '*')}")

    @staticmethod
    def start_menu():
        """lists the choices
        Print:
            str: start_menu """
        start_menu = "> [1]Player list  [2]Tournament  [3]Match  [4]Quit <"
        print(f"\n{start_menu.center(106, '-')}")

    @staticmethod
    def input_int():
        """Select the choice you want to make
        Return:
            int: choice """
        input_int = input(f"Please enter an choice : ").capitalize()
        input_int = int(input_int)
        return input_int

# Integration of functions
    @staticmethod
    def next_run():
        GlobalApp.reception()
        GlobalApp.choice()
        GlobalApp.start_menu()
        choice = GlobalApp.input_int()
        choice = int(choice)
        return choice
