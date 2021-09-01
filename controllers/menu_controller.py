from views.menu_views import MenuViews


class menu_controller():
    
    def __init__(self, view):
        self.view = view

    def first_menu(self):
        self.view.main_menu()
        choice = input()

        if choice == '1':
            print('choix 1')
            self.create_tournament()
        elif choice == '2':
            print('choix 2')
        else:
            self.first_menu()

    def create_tournament(self):
        self.view.create_tournament()
        

    def run_application(self):
        self.view.welcome()
        self.first_menu()