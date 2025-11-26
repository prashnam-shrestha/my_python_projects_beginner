import random

def roll_dice():
    return (random.randint(1,6),random.randint(1,6))

count = 0

while True:

    choice = input('Roll a dice? (y/n):').lower()

    if choice == 'y':
        try: 
         num =int(input('How many times?:'))
        except ValueError:num = 0

        for i in range(num):
            print(roll_dice())
        count+=num

    elif choice == 'n':
        print('Thanks for playing!')
        print(f'Dice rolled:{count}times!')
        break
    else:print('Invalid choice!')
       


