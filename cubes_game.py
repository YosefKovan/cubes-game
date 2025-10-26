import random 


def roll_two_d6():
   """rolls two dice and returns the result"""
   dice1 = random.randrange(1,7)
   dice2 = random.randrange(1,7)
   return dice1, dice2 


def add_dice_result(dices):
   """this will return the result of the dice"""
   return dices[0] + dices[1]


def is_bust(score):
   """check if score passe dma score """
   max_score = 100
   
   return score > max_score


def is_exact_100(score):
   """this function checks if the score equals max score"""
   max_score = 100
   return score == max_score 



def closer_to_target(a, b, target=100):
   """checks which is closer to the target"""
   
   #this will return None if one of the sores are 
   #larger then the target
   if a > target or b > target:
      return None 

   a_difference = target - a
   b_difference = target - b
   
   #the number that is closer the difference will be smaller.
   if a_difference < b_difference:
      return 1
   elif b_difference < a_difference:
      return 2
   else: 
      return None
   



def tie_breaker(roller):
   
   print("A tie occured will roll the dice to brake the tie")
   tie_broken = False

   while not tie_broken:
      
      p1_dice1, p1_dice2 = roll_two_d6()
      p2_die1, p2_dice2 = add_dice_result(roll_two_d6())
      
      if p1_dice1 + p1_dice2 > p2_die1 + p2_dice2:
         print("player1 rolled ")
         return 1
      elif p2_die1 + p2_dice2 > p1_dice1 + p1_dice2:
         return 2
      else:
         print("results are equal trying again!")
   
   
   

def turn_decision(input_fn):
   
   user_msg = "Please enter 'r' to roll, or 'p' to pass your turn: "
   valid_input = False

   while not valid_input:
      
      user_input = input(user_msg)

      if user_input == 'r' or user_input == 'p':
        return user_input
     


def handle_end(player1, player2):
   """this function will find the winner in case that two passes ocured """
   
   if player1["score"] > player2["score"]:
      print(f"player1 score - {player1["score"]}, player2 score - {player2["score"]}, PLAYER 1 WON")

   elif player1["score"] < player2["score"]:
       print(f"player1 score - {player1["score"]}, player2 score - {player2["score"]}, PLAYER 2 WON")
   else:
      result = tie_breaker()

      if result == 1:
         print(f"player1 score - {player1["score"]}, player2 score - {player2["score"]}, PLAYER1 WON")
      else:
         print("player 2 won")    


            
def handle_turn(player, player_data):
     
     if player == 0:
        print("its player 1 turn")
     else:
        print("player 2 turn ")   

     turn_choice = turn_decision()

     if turn_choice == 'p':
        return "PASS"
     else:
        dice1, dice2 = roll_two_d6()

        print(f"Deice rolled {dice1} {dice2} - ", end="")
        player["score"] += dice1 + dice2
        
        if player["score"] == 100:
           return "WON"
        elif  player["score"] > 100:
           return "LOST"

        
              
def play_round(players):
   
   passes = 0

   for i in range(0, 2):
        

        turn_decision = handle_turn(i ,players[i]) 
        match turn_decision:
           case "PASS":
              passes += 1
           case "WON":
              print(f"player 1 score - {players[0]["score"]} , player 2 score - {players[1]["score"]}, PLAYER {i} WON!")
              return False
           case "LOST":
              print(f"player 1 score - {players[0]["score"]} , player 2 score - {players[1]["score"]}, PLAYER {i} LOST!")


   if passes == 2:
      handle_end()
       
                  
    
def play_game():
   
   game_over = False

   players = [{"player" : "player1", "score" : 0}, {"palyer" : "player2", "score" : 0}]

   while not game_over:
       play_round(players)
          

          

if __name__ == "__name__":
   pass