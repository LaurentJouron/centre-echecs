from view.global_app import GlobalApp


class StartApp:
    @staticmethod
    def first_run():
        GlobalApp.start_app()

    @staticmethod
    def next_run():
        GlobalApp.reception()
        GlobalApp.choice()
        GlobalApp.start_menu()
        choice = GlobalApp.input_int()
        choice = int(choice)
        return choice
