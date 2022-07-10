import random
# crit fail

def verbose(arg):
    if arg == 1:
        print(f' You did roll {arg} - Critical fail!')
    elif arg == 6:
        print(f' You did roll {arg} - Critical hit!')
    else:  
        print(f'You rolled a {arg}')
    return 0


def main():
    dice_rolls=int(input(' How many dice would like to roll?  '))
    dice_size=int(input(' How many sides are the dice  '))
    dice_sum=0

    for each in range(0,dice_rolls):
        roll=random.randint(1,dice_size)
        dice_sum+=roll
        verbose(roll)
        
    print(f'Your total roll is {dice_sum}')

if __name__== "__main__":
    main()
