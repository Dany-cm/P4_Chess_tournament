from views.menu_views import MenuViews

class menu_controller():
    
    def __init__(self):
        self.main_view = MenuViews()

    def first_menu(self):
        self.main_view
        choice = input()

        if choice == '1':
            print('choix 1')
        else:
            self.first_menu()