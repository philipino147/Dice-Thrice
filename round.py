import random 
import time
#input("place input here")

'''Dice Rules 
Objective: First to 5500 points wins
First Roll is 3 dice
Any dice that is a 1 counts as 100 points
Any dice that is a 5 counts as 50 points
Rolling 2,4,6 results in a reroll
Rolling three 2s counts as 200 points and reroll
Rolling three 3s counts as 300 points and reroll
Rolling three 4s counts as 400 points and reroll
Rolling three 5s counts as 500 points and reroll
Rolling three 6s loses all current points in the game
Rolling three 1s counts as 1000 points and reroll
Rolling three consecutive numbers (1,2,3) counts as 200 points and a reroll
'''

#Generate a Roll and return it
def dice_Roll(i):
  roll = []
  for x in range(i):
    roll.append(random.randint(1,6))
  roll.sort()
  roll = tuple(roll)
  #checkRoll(roll,score)
  return roll

#Roll 3 dice and check if there is a special rolling case. If yes, then add points to the standby score and automatically generate a new roll. Otherwise, continue the rolling procedure
def new_Turn(player,score,strategy):
  standbyscore = 0
  reroll = 1
  dice_number = 3
  while(reroll == 1):
    print("Rolling %s dice..." % dice_number)
    print("Strategy is: %s" % strategy)
    tup = dice_Roll(dice_number)
    currentscore = rollscores.get(tup,0)
    time.sleep(2)
    print(tup)
    if(currentscore < -2):
      currentscore = currentscore*-1
      print("Adding %s and Re-Rolling" % currentscore)
      standbyscore = standbyscore + currentscore
      print("Score is %s before Re-Rolling" % standbyscore)
    elif(tup == (2,4,6)):
      print("Re-Rolling")
      standbyscore = standbyscore + currentscore
      print("Score is %s before Re-Rolling" % standbyscore)
    elif(tup == (6,6,6)):
      print("Sorry! You Lost All Points")
      score = 0
      break
    elif(dice_number == 0):
      print("No more Dice!")
      break
    elif(currentscore > 0):
      ones = tuplecounter(tup,1)
      fives = tuplecounter(tup,5)
      ones_and_fives = int(ones + fives)
      roll_Size = len(tup)
      next_roll_size = roll_Size - ones_and_fives
      if(next_roll_size == 0):
        print("Congrats! No more Dice")
        standbyscore = standbyscore + currentscore
        break
      print("There are %s ones and %s fives" % (ones,fives))
      print("You can add %s Extra Points...or... Continue Rolling" % (currentscore+standbyscore))
      if(player["playertype"] == "h"):
        choice = user_choice()
        time.sleep(1)
        print("You chose %s" % choice)
      else:
        strategic_score = currentscore+standbyscore
        print("Strategic Score: %s" % strategic_score)
        choice = strategic_choice(strategy,strategic_score,tup)
        time.sleep(1)
        print("%s was chosen" % choice)
        strategic_score = 0
      time.sleep(1)
      if(choice == "y"):
        dice_number = continue_Roll(next_roll_size)
        standbyscore = standbyscore + currentscore
      elif(choice == "n"):
        print("Ok...")
        standbyscore = standbyscore + currentscore
        break
    else:
      print("No more Re-Rolls! You lost your chance for points this turn...")
      reroll = 0
      standbyscore = 0
  time.sleep(1)
  score = score + standbyscore
  #print("The Standby Score to add is now %s" % standbyscore)
  return score

#Determines whether to answer yes or no to a continued roll based on the computer's set strategy
def strategic_choice(strategy,standbyscore,tuple_roll):
  if(strategy == "balanced"):
    print("Balanced Answer")
    if(standbyscore >= 150):
      return "n"
    else:
      return "y"
  elif(strategy == "aggressive"):
    print("Aggressive Answer")
    if(standbyscore >= 250):
      return "n"
    else:
      return "y"
  elif(strategy == "conservative"):
    print("Conservative Answer")
    if(standbyscore >= 100):
      return "n"
    else:
      return "y"
  elif(strategy == "random"):
    print("Random Choice")
    choice_list = ["y","n"]
    answer = random.choice(choice_list)
    return answer
  else:
    print("Timid Strategy: Selecting 'n'")  
    return "n"

#Checks how many instances of a specific value are found in a tuple
def tuplecounter(tup, en): 
    return tup.count(en)  

#Takes and validates a yes or no answer from the player then returns it  
def user_choice():
  while True:
    try:
      choice = str(input("Continue Rolling? (y/n)"))
      if(choice == "y" or choice == "n"):
        break
      print("Invalid choice entered, enter 'y' or 'n'")
    except Exception as e:
      e = "The choice must be 'y' or 'n', you typed in %s" % choice
      print(e)
  return choice    

#Used if the player wishes to roll remaining dice
#Count the number of 1s and 5s in the tuple
#Subtract the # of 1s and 5s to from the current tuple length to get
#the amount of dice that will be rolled next

#If not a reroll case, check if 1s or 5s exist, then ask if player wishes to continue rolling
#To continue a roll, add any 5s or 1s to the standby score then pass how many dice are left and the new standby score. 

def continue_Roll(next_roll_size):
  """ones = tuplecounter(tup,1)
  fives = tuplecounter(tup,5)
  ones_and_fives = int(ones + fives)
  roll_Size = len(tup)
  #print(roll_Size)
  next_roll_size = roll_Size - ones_and_fives
  currentscore = rollscores.get(tup,0)
  #print("Adding %s Points" % currentscore)
  score = score + currentscore
  #print("Score is %s before Re-Rolling" % score)"""
  if(next_roll_size == 2):
      return 2
  elif(next_roll_size == 1):
      return 1
  else:
    return 0

#Cases Dictionary
rollscores = {
    (1,1,1): -1000,
    (1,1,2): 200,
    (1,1,3): 200,
    (1,1,4): 200,
    (1,1,5): 250,
    (1,1,6): 200,
    (1,2,2): 100,
    (1,2,3): -200,
    (1,2,4): 100,
    (1,2,5): 150,
    (1,2,6): 100,
    (1,3,3): 100,
    (1,3,4): 100,
    (1,3,5): 150,
    (1,3,6): 100,
    (1,4,4): 100,
    (1,4,5): 150,
    (1,4,6): 100,
    (1,5,5): 200,
    (1,5,6): 150,
    (1,6,6): 100,
    (2,2,2): -200,
    (2,2,5): 50,
    (2,3,4): -200,
    (2,3,5): 50,
    (2,4,5): 50,
    (2,4,6): 0,
    (2,5,5): 100,
    (2,5,6): 50,
    (3,3,3): -300,
    (3,3,5): 50,
    (3,4,5): -200,
    (3,5,5): 100,
    (3,5,6): 50,
    (4,4,4): -400,
    (4,4,5): 50,
    (4,5,5): 100,
    (4,5,6): -200,
    (5,5,5): -500,
    (5,5,6): 100,
    (5,6,6): 50,
    (1,1): 200,
    (1,2): 100,
    (1,3): 100,
    (1,4): 100,
    (1,5): 150,
    (1,6): 100,
    (2,5): 50,
    (3,5): 50,
    (4,5): 50,
    (5,5): 100,
    (5,6): 50,
    (1,): 100,
    (5,): 50
}
