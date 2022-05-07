from view.global_app import GlobalApp


class StartApp:
    @staticmethod
    def first_run():
        GlobalApp.start_app()

    @staticmethod
    def next_run():
        choice = GlobalApp.next_run()
        return choice
