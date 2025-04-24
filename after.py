import random 
from reza import starting_card
from reza import blackjack
from reza import total
from reza import user_card
from reza import system_card
from reza import comparison




def Blackjack_game():
    if  input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y" :
        game = True
    else :
        game = False
        print("End Of Game")
        return
    while game :
        
        user = 0
        
        system = 0 

        user = starting_card(user)
        
        system = starting_card(system)
        
        total_user = 0
        
        total_system = 0
        
        total_user = total(user,total_user)
        
        total_system = total(system,total_system)
        
        game= blackjack(total_user,"you",game)

        if game == False:
            Blackjack_game()
            return
        
        total_user = user_card(user,total_user,system)

        if total_user == False :
            Blackjack_game()
            return
        
        game = blackjack(total_system,"computer",game)

        if game == False :
            Blackjack_game()
            return
        
        system = system_card(system,total_system,total_user)
        
        game = comparison(total_system,total_system,system,user,game)
        
    print("End Of Game")
    
Blackjack_game()

    