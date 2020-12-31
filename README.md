# Dice-Thrice
A fun text-based Dice Game

To play, just follow these steps:

1.  Download and Extract the folder containing the game files.
2.  Navigate to the folder and using the terminal, run the main.py file using python 3.
    (Use the command: "py .\main.py")
3.  A default game will start with one human player vs 3 computers that each use a different strategy.
4.  A custom-game can be started by editing the main.py file and commenting out 'default' while commenting in 'custom' on Line 10
    Also make sure to change Line 13 playerlist = custom (instead of default).

****Example: Original Lines 9-13 look like this****

default = player.defaultboard()
#custom = player.playerboard()

#The dictionary of players
playerlist = default

****Change them to look like this****

#default = player.defaultboard()
custom = player.playerboard()

#The dictionary of players
playerlist = custom

  5. To change back to a default game simply reverse the settings
  6. Enjoy!!
