import random
num = int(random.randint(0, 100))
while True:
    while True:
        try:
            guess = int(input('enter a num from 0 to 100 '))
            break
        except:
            print('not a number')
    guess = num - guess
    if guess < 0:
        print('lower')
    elif guess > 0:
        print('higher')
    else:
        print('youre correct!')
        break
