# Dice-Thrice
A fun text-based Dice Game

# Dice Rules 
          *Objective: First to 3000 points wins
          
          *First Roll is 3 dice (displayed as 3 numbers n,n,n)
          *Any dice that is a 1 counts as 100 points
          *Any dice that is a 5 counts as 50 points
          *Rolling 3 dice with one 2, one 4, and one 6 results in an automatic reroll
          *Rolling three 2s counts as 200 points and an automatic reroll
          *Rolling three 3s counts as 300 points and an automatic reroll
          *Rolling three 4s counts as 400 points and an automatic reroll
          *Rolling three 5s counts as 500 points and an automatic reroll
          *Rolling three 6s loses all current points in the game
          *Rolling three 1s counts as 1000 points and an automatic reroll
          *Rolling three consecutive numbers (1,2,3) counts as 200 points and an automatic reroll
          *Any combination of 1s and 5s in the dice roll gives 
           the player an option to continue rolling the remaining dice
          *If a player continues rolling and scores no points, (by rolling 1s and 5s)
           they lose any points gained during that turn

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
