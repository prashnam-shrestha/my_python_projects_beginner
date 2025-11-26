#loop main with choice
    #1 play 
    #play - loop(1time)
    #2 bestscore- best score in different levels
    #3 difficulty - hard1-100(8 attempts) -medium 30-70(10 attempts) - easy (50-60) (15attempts) d
    #default = medium
    #4 simple exit with break
#start time 12:47pm

import random

best_score = 0 #until the game exits
difficulty = 2

#--Helper functions--
def get_valid_input(text):
    while True:
        try:
            return int(input(text))
        except ValueError: print('Invalid choice!\n')


def best_score_comparison(user_attempt):
    global best_score
    
    if best_score == 0:
        best_score = user_attempt
        return user_attempt

    elif (user_attempt<best_score) and (best_score != 0):
        best_score = user_attempt
        return user_attempt
    else: return False

#Main functions
def main():
    print('--Guessing game--')
    print('1:PLAY')
    print('2:BEST SCORE')
    print('3:DIFFICULTY')
    print('4:EXIT\n')
    return get_valid_input('Enter your choice(1 ~ 4):')

def play():
    global best_score

    range_value_min , range_value_max = 0,0
    user_attempts_limits = 0
    

    if  difficulty == 1:
        range_value_min,range_value_max = 20,30
        user_attempts_limits += 15
        print('Difficulty - Easy\n')
    elif difficulty == 2:
        range_value_min,range_value_max = 30,70
        user_attempts_limits += 10
        print('Difficulty - Medium (default) \n')
    elif difficulty == 3:
        range_value_min,range_value_max = 1,100
        user_attempts_limits += 8
        print('Difficulty - Hard\n')

    number_to_guess = random.randint(range_value_min,range_value_max)

    i = 0
    user_attempts = 0 #later for best score
    while i<user_attempts_limits:
        user_guess = get_valid_input(f'Guess the number between {range_value_min} and {range_value_max}:')
        print()
        close_guesses = []        
        for j in range(number_to_guess-10,number_to_guess+11):
            close_guesses.append(j)

        #High or Low only for close guesses
        if (user_guess in close_guesses and user_guess < number_to_guess):
            print('Incorrect. Try again!')
            print('Feedback: Your guess is lower.\n')
        elif (user_guess in close_guesses) and (user_guess > number_to_guess):
            print('Incorrect. Try again!')
            print('Feedback: Your guess is higher.\n')

        #Too high or Too low for bad guesses
        elif (user_guess not in close_guesses) and (user_guess > number_to_guess):
            print('Incorrect. Try again!')
            print('Feedback: Your guess is too high.\n')
        elif (user_guess not in close_guesses) and (user_guess < number_to_guess):
            print('Incorrect. Try again!')
            print('Feedback: Your guess is too low.\n')
        elif user_guess == number_to_guess:
            user_attempts = (i+1)
            print('Congratulations!')
            print(f'Feedback: Nice, You guessed it in {user_attempts} attempts!')
            
            if best_score_comparison(user_attempts):
                print(f'New best score: {user_attempts} attempts!\n ')
                best_score = user_attempts
            break
            
        else:
            print('Incorrect. Try again!')
            print('Feedback: Please enter a number.\n')
  
        i += 1
    if i == user_attempts_limits:
        print(f'You ran out of attempts.\nTry again!\n')


def best_score_view():
    print(f'Best score of all time: {best_score} attempts!\n')

def choose_difficulty():
    global difficulty 
    print('--Difficulty levels--')
    print('1. Easy\n2. Medium\n3.Hard')
    user_preference = get_valid_input(('Enter difficulty level(1 2 3):'))
    print()
    if user_preference == 1 :
        difficulty = 1
    elif user_preference == 2:
        difficulty = 2
    elif user_preference == 3:
        difficulty = 3
    else: print('Please enter between 1 - 3!\n')
    print("-New difficulty set-\n")

while True:
    choice = main()

    if choice == 1:
        play()
    elif choice == 2:
        best_score_view()
    elif choice == 3:
        choose_difficulty()
    elif choice == 4:
        print('Thank you for playing!\n')
        break
    else: print('Please enter between(1 ~ 4)!\n')

#finish time - 14:15 pm
