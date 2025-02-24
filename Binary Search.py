import random as rd

target = rd.randint(1,100)

low_lim,high_lim = 1,100

while low_lim <= high_lim:
    guess = (low_lim + high_lim) // 2
    if guess < target:
        low_lim = guess + 1
    elif guess > target: 
        high_lim = guess - 1
    else:
        print(guess)
        break