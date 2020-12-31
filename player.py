import json

def new_player():
  while True:
    playername = input("Player's Name: ")
    if playername.isalpha():
      if len(playername) < 8:
        break
      else:
        print("Length of string must be less than 8")
    print("Please enter characters A-Z only")
  playertype = player_choice()
  strategy = ""
  if(playertype == "h"):
    strategy = "human"
  else:
    strategy = strategy_choice(playername)
  player = {
    "playername": playername,
    "playertype": playertype,
    "score": 0,
    "strategy": strategy
  }
  return player

def player_choice():
  while True:
    try:
      choice = str(input("Player Type(h/b): "))
      if(choice == "h" or choice == "b"):
        break
      print("Invalid choice entered, enter 'h' or 'b'")
    except Exception as e:
      e = "The choice must be 'h' or 'b', you typed in %s" % choice
      print(e)
  return choice

def strategy_choice(name):
  while True:
    try:
      choice = str(input("%s's Strategy (aggressive,balanced,conservative,random): " % name))
      if(choice == "aggressive" or choice == "balanced" or choice == "conservative" or choice =="random"):
        break
      print("Invalid choice entered, enter aggressive/balanced/conservative/random")
    except Exception as e:
      e = "The choice must be any of these: aggressive/balanced/conservative/random, you typed in %s" % choice
      print(e)
  return choice        

#Create a custom number of players
def playerboard():
  playerlist = {}
  max_players = 5
  while True:
    try:
      num = input("Number of Players: ")
      num = int(num)
      if(type(num) == int and num < max_players):
        break
      print("Enter a number below %s" %max_players) 
    except Exception as e:
      e = "The number must be an integer below %s, you typed in %s" % (max_players,num)
      print(e)
  for x in range(num):
    key = "player" + str(x+1)
    print(key)
    playerlist[key] = new_player()
  return playerlist

#Initialize a game against the computer
def defaultboard():
  playerlist = {
    "player1":{
      "playername": "Player1",
      "playertype": "h",
      "score": 0,
      "strategy": "human"
    },
    "player2":{
      "playername": "Computer1",
      "playertype": "b",
      "score": 0,
      "strategy": "aggressive"
    },
    "player3":{
      "playername": "Computer2",
      "playertype": "b",
      "score": 0,
      "strategy": "conservative"
    },
    "player4":{
      "playername": "Computer3",
      "playertype": "b",
      "score": 0,
      "strategy": "random"
    }   
  }
  return playerlist

#print(json.dumps(playerboard(), indent=4))
#print(new_player)