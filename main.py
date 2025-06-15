from random import randint





while True:

    while True:
        user_choice = input("Which level do you want to choose?: hard, medium, easy:").lower()

        if user_choice in ['hard', 'medium', 'easy']:
            break
        else:
            print("Invalid input! Please choose again.")

    if user_choice == 'easy':
        max_number = 50
        guess_limit = 10

    elif user_choice == 'medium':
        max_number = 100
        guess_limit = 7

    else: 
        max_number = 200
        guess_limit = 5




    secret_number = randint(1,max_number)

    number = 0

    while number < guess_limit :

        user_guess = int(input("enter a number: "))
        number += 1
        if user_guess > secret_number:
            print("The number you guessed is greater than the hidden number.")
        
        elif user_guess < secret_number:
            print("The number you guessed is smaller than the hidden number.")
        else: 
            print("You guessed it right.")
            break


    if user_guess != secret_number :
        print("The number of times you were allowed to guess is over!")

    while True:
        play_again = input("Do you want to play again? yes, no").lower()
        if play_again in ["yes", "no"]:
            break
            
        else: 
            print("Invalid input! Please choose again.")

    if play_again == 'no':
        break
    
        
        

    


