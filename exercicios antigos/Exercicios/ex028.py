from random import randint
chosen = randint(0,5)
print('I chose a number between 0 and 5! Try guessing it!')
guess = int(input('Your guess: '))
if guess == chosen:
    print(f'You got it! I did choose the number {chosen}')
else:
    print(f'WROOOONG! I thought of the number {chosen}')
