import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def starting_card(user):
    user = []
    for chance in range(0,2):
        new = random.choice(cards)
        user.append(new)
    return user

def first_print_score(user,total_user,system):

    print(f"Your cards: {user}, current score: {total_user}")

    print(f"Computer's first card: {system[0]} computer Score : {system[0]}")


def print_blackjack(gamer):

    print(f"{gamer} has a Blackjack")

    print(f"{gamer} Win !")




def print_cpmputer_win(user,total_user,system,total_system):
    print(f"Your cards: {user}, current score: {total_user}")

    print(f"Computer cards: {system} computer Score : {total_system}")

    print("You lose !")


def print_user_win(user,total_user,system,total_system):
    print(f"Your cards: {user}, current score: {total_user }")

    print(f"Computer cards: {system} computer Score : {total_system}")

    print("You Win !")


def print_score(user,total_user,system):

    print(f"Your cards: {user}, current score: {total_user}")

    print(f"Computer's first card: {system[0]}")


def print_draw(ali ,total_ali,computer,total_computer):

    print(f"Your cards: {ali}, current score: {total_ali}")

    print(f"Computer cards: {computer} computer Score : {total_computer}")

    print("Draw")



def total(gamer,zero):
    '''give list and collects its element'''
    zero = 0

    for i in gamer:

        zero += i

    return zero



def choice_card(list):
    '''Choice Random card in card list'''

    for i in range(0,1):

       list.append(random.choice(cards))


def user_card(list,total_user,system):
    '''Add card to user or computer'''

    first_print_score(list, total_user,system)


    
    condition = True

    while condition  :


        if input("Do you Want Give a card ?") == "y" :

            choice_card(list)
            total_user = total(list,total_user)
            
            var = 0
            if total_user > 21 :
                for i in list:
                    if i == 11:
                        list[var] = 1
                        total_user = total(list,total_user)
                    var += 1
                    
        

            first_print_score(list, total_user,system)
                    

            if total_user > 21 :
                print("you Lose !")

                total_user = False

                return total_user
        else :
            return total_user



def blackjack(totally,gamer,Bolean):
    
    if totally == 21 :
        print_blackjack(gamer)
        Bolean = False
        return Bolean
    return Bolean  


def system_card(list,total_system,total_user):
    condition = True
    while condition :
        if total_system > 21 :
            var = 0

            for i in list:

                if i == 11:

                    list[var] = 1
                var += 1
        total_system = total(list,total_system)        
        if total_system < total_user :
            choice_card(list)
            total_system = total(list,total_system)

        else: 
            condition = False
    return list



def comparison(total_system,total_user,system,user,bolean):

    total_system = total(system,total_system)
    total_user = total(user,total_user)

    if total_system > 21 :
        print_user_win(user,total_user,system,total_system)
    elif total_system > total_user :
        print_cpmputer_win(user,total_user,system,total_system)

    if total_system == total_user :
        print_draw(user,total_user,system,total_system)

    if input("Do You wann Play again a blackjack Game ? Type 'y' to play type 'n 'to exit : ") == "y" :
        return bolean
    else:
        bolean = False
        return bolean
    

