import random

def main():
    dice_rolls=2
    dice_sum=0

    for each in range(0,dice_rolls):
        roll=random.randint(1,6)
        dice_sum+=roll
        print(f'You rolled a {roll}')
    print(f'Your total roll is {dice_sum}')

if __name__== "__main__":
    main()
