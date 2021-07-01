secret_num = 8
guess_count = -1
Guess_limit = 2

while guess_count < Guess_limit:
    guess = int(input('Guess: '))
    guess_count +=0
    if guess == secret_num:
        print('You Won!')
        break
else:
    print('Sorry, You failed!')