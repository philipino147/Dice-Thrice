import round
import player
import time
import os
import json

new_Turn = round.new_Turn
new_player = player.new_player
default = player.defaultboard()
#custom = player.playerboard()

#The dictionary of players
playerlist = default

#Initializes the scoreboard with each player's name and score
scoreboard = {}

#Updates the scoreboard with the current standings
def update_scoreboard():
  for player in playerlist:
    name = playerlist[player]["playername"]
    scoreboard[name] = playerlist[player]["score"]

#Generate a turn for each player
#Rolls and Updates the scores for each player
def new_round(score,round):
  for player in playerlist:
    print("ROUND %s" % round)
    print("%s's Turn..." % playerlist[player]["playername"])
    time.sleep(1)
    totalscore = playerlist[player]["score"]
    update_scoreboard()
    print("Scoreboard: %s" % scoreboard)
    #print("Current Score: %s" % totalscore)
    new_score = new_Turn(playerlist[player],totalscore,playerlist[player]["strategy"])
    print("%s's Total Score is now %s" % (playerlist[player]["playername"],new_score))
    playerlist[player]["score"] = new_score
    time.sleep(2)
    os.system("clear")
    if(playerlist[player]["score"] >= score):
      print("%s wins!!" % playerlist[player]["playername"])
      return
    else:
      continue   
  return

#Generates a new game 
def new_game():
  winning_score = 5500
  round = 1
  max_round = 200
  print("""Dice Rules 
          Objective: First to %s points wins
          First Roll is 3 dice
          Any dice that is a 1 counts as 100 points
          Any dice that is a 5 counts as 50 points
          Rolling 3 dice with one 2, one 4, and one 6 results in a reroll
          Rolling three 2s counts as 200 points and reroll
          Rolling three 3s counts as 300 points and reroll
          Rolling three 4s counts as 400 points and reroll
          Rolling three 5s counts as 500 points and reroll
          Rolling three 6s loses all current points in the game
          Rolling three 1s counts as 1000 points and reroll
          Rolling three consecutive numbers (1,2,3) counts as 200 points and a reroll
          Any combination of 1s and 5s in the dice roll gives 
          the player an option to continue rolling the remaining dice
          If a player continues rolling and scores no points (by rolling 1s and 5s)
          they lose any points gained during that turn)
          """ % winning_score)
  input("press ENTER to continue...")
  #for x in playerlist.values():
  #  print(x["score"])
  while (not any(v["score"] >= winning_score for v in playerlist.values())):
    print("*** ROUND %s ***" % round)
    time.sleep(2)
    os.system("clear")
    new_round(winning_score,round)
    round = round + 1
    if(round > max_round):
      print("Max Round Reached")
      break
  print("Final Results: %s" % json.dumps(playerlist, indent=4))
  data = playerlist
  with open('game_results.json', 'w') as fp:
     json.dump(data, fp)
  round = round -1
  print("Rounds Played: %s" % round)
  
new_game()