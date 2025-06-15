from random import randint





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
        print("adad shama bozorgtar hast!")
        
    elif user_guess < secret_number:
        print("adad shoma koochaktar hast!")
    else: 
        print("shoma dorost hads zadid!")
        break
if user_guess != secret_number :
    print("tedad hads haye shoama tamam shod!")
    
        
        

    


