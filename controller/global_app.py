from view.global_app import GlobalApp


def first_run():
    GlobalApp.start_app()
    GlobalApp.reception()
    GlobalApp.choice()
    GlobalApp.start_menu()
    input: int = GlobalApp.input()
    return input


def next_run():
    GlobalApp.reception()
    GlobalApp.choice()
    GlobalApp.start_menu()
    input: int = GlobalApp.input()
    return input
