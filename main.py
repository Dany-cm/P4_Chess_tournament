from controllers.menu_controller import menu_controller
from views.menu_views import MenuViews
from models.players import Player, create_new_player, load_players

def  __init__(self):
    pass

def main():
    #print('need title')
    #menu = menu_controller(MenuViews())
    #menu.first_menu()
    load_players()

    create_new_player('f','f','2021/02/21','M')
    create_new_player('D','D','2021/05/11','M')
    create_new_player('Z','Z','2021/12/21','M')



if __name__ == "__main__":
    main()
