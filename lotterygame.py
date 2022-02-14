
# Lottery game
# which gives you hint on
# number for lottery ticket

# Asks us how much we want to pay
# and we get that many ticket

# more or less 
# may be show us our budget
# and for each ticket cost 10 $

# if we guess it right we win 
# 1000,000$ 
# and it gets added to our budget


# I want you to create a to do list
#  yourself and start creating this game !

# you can create your own
# ASCII art using this link:

# http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
# and also change fonts !

# font I used: Big Money-ne

logo = """

/$$                   /$$     /$$                                                      /$$$$$$                                   
| $$                  | $$    | $$                                                     /$$__  $$                                  
| $$        /$$$$$$  /$$$$$$ /$$$$$$    /$$$$$$   /$$$$$$  /$$   /$$                  | $$  \__/  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ 
| $$       /$$__  $$|_  $$_/|_  $$_/   /$$__  $$ /$$__  $$| $$  | $$                  | $$ /$$$$ |____  $$| $$_  $$_  $$ /$$__  $$
| $$      | $$  \ $$  | $$    | $$    | $$$$$$$$| $$  \__/| $$  | $$                  | $$|_  $$  /$$$$$$$| $$ \ $$ \ $$| $$$$$$$$
| $$      | $$  | $$  | $$ /$$| $$ /$$| $$_____/| $$      | $$  | $$                  | $$  \ $$ /$$__  $$| $$ | $$ | $$| $$_____/
| $$$$$$$$|  $$$$$$/  |  $$$$/|  $$$$/|  $$$$$$$| $$      |  $$$$$$$                  |  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$$
|________/ \______/    \___/   \___/   \_______/|__/       \____  $$                   \______/  \_______/|__/ |__/ |__/ \_______/
                                                           /$$  | $$                                                              
                                                          |  $$$$$$/                                                              
                                                           \______/                                                               
"""
import random
print(logo)
print("Welcome to our lottery game :) ")
budget = 100

def game():
    global budget
    ticket_count = input(f"Each ticket costs 10$ and your current budget is {budget} $\nENTER NUMBER OF TICKETS YOU WANT TO BUY ==>")
    ticket_count = int(ticket_count)
    ticket_price = ticket_count *10


    lottery_number = random.randint(0,100)
    # print("Pstttt.... the lottery number is ", lottery_number)

    if (ticket_count * 10 > budget):
        print(f"Unable to make purchase. Total ticket price was {ticket_price} $ higher than your budget of {budget} $")

    else:
        budget = budget - ticket_price
        print(f"==>You bought {ticket_count} tickets worth {ticket_price} $")
        print(f"==>Your new budget is {budget} $")

        continue_game = True

        while ticket_count >0 and continue_game == True:
            ticket_count = ticket_count - 1
            user_entry = input("Pick up your number for lottery ticket (Between 0 - 100): ")
            
            user_entry = int(user_entry)
            # evaluate_number (user_entry, lottery_number, ticket_count)
            if user_entry == lottery_number:
                budget = budget + 1000000
                print(f"Congrats!! You won a lottery for 1 million dollars!! Your new budget is {budget} $")
                continue_game = False
                    
            elif user_entry < lottery_number:
                print(f"Ummmm.... Your guess is too low")
                print(f"You have {ticket_count} choices left")
                if (ticket_count == 0):
                    print(f"The correct number was {lottery_number}")
                    print("Better luck next time. Try again !!!")
            
            else:
                print(f"Oh nooo.. Your guess is too high")
                print(f"You have {ticket_count} choices left")
                if (ticket_count == 0):
                    print(f"The correct number was {lottery_number}")
                    print("Better luck next time. Try again !!!")
    
game()

continue_again = True
while budget >=10 and continue_again == True:
    user_input = input (f"You have {budget} $ left , would you still like to continue the game? (y/n)").lower()

    if (user_input=='y'):
        game()
    else:
        continue_again = False
        print(f"You now have {budget} $ in your bank :) ")