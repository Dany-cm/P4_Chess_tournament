# Develop a Chess tournament software in Python

<p align="center">
  <img width="460" height="300" src="https://user.oc-static.com/upload/2020/09/22/16007793690358_chess%20club-01.png">
</p>

This application allows you to manage a tournament using the Swiss-system.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required dependencies.

```bash
pip install -r requirements.txt
```

## Usage

```python
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
venv\Scripts\activate

# Install required packets
pip install -r requirements.txt

# Start the application
python main.py
```

## Menu

In order to navigate in the menu, simplify enter the number of the menu you wish to enter.

For example:
```
Welcome to the chess manager application

What do you want to do?
1: Manage tournaments
2: Manage players
3: Reports
4: Quit application
```
Entering '1' in the application will redirect you in 'Manage tournaments' menu
```
What do you want to do?

1: Create a tournament
2: Add 8 players to a tournament
3: Start a tournament
4: Resume a tournament
5: Back to previous menu
```

## Creating a tournament

Before creating a tournament, you will first need to create 8 players, simply navigate to 'Manage players' -> 'Create a new player', after creating the 8 required players navigate to tournament menu, you will be see 4 possible choices, select 'Create a tournament' fill the information and when you're done you can add the 8 players you created to the tournament.

## Start the tournament
Navigate to 'Manage tournaments' -> 'Start a tournament', if you correctly filled all the information above, you will see your tournament name.
```
Choose a tournament

1: Tournoi de Paris
```
In mine it's 'Tournoi de Paris' select it. Now navigate to 'Manage tournament' again and chose 'Resume a tournament'
```
Choose a tournament

1: Tournoi de Paris
```

Once you select 'Resume a tournament' you will be asked to select which player won or if it's a draw.

```
Please input the result (typing 1, 2 or 3) for the following match
Francis Aubry vs Gabriel Vincent
1 - Francis Aubry won
2 - Gabriel Vincent won
3 - Draw
```
You will have to repeat this step until you reach the last round, you will be asked to enter the new rank for each player
```
Match result updated successfully

Enter the new rank for Aubry Francis: 234
Aubry Francis rank has been updated to 234
Enter the new rank for Schneider Martin: 543
Schneider Martin rank has been updated to 543
Enter the new rank for Vasseur Jean: 234
Vasseur Jean rank has been updated to 234
Enter the new rank for Deschamps Marius: 654
Deschamps Marius rank has been updated to 654
Enter the new rank for Vincent Gabriel: 876
Vincent Gabriel rank has been updated to 876
Enter the new rank for Renaud Thomas: 123
Renaud Thomas rank has been updated to 123
Enter the new rank for Garcia Jade: 756 
Garcia Jade rank has been updated to 756
Enter the new rank for Laporte Emma: 654
Laporte Emma rank has been updated to 654
```

## Reports
The report menu shows you all players(by alphabetical or rank order), all players in a tournament(by alphabetical or rank order), all tournament, all rounds/match from a tournament.
```
What do you want to do?

1: Show all players
2: Show all players in a tournament
3: Show all tournament
4: Show all rounds from a tournament
5: Show all matches from a tournament
6: Back to the previous menu
```
## License
[Danycm1](https://choosealicense.com/licenses/mit/)
