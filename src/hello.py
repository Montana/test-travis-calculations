import random
choices = list(range(100))
random.shuffle(choices)
print(choices.pop())
while choices:
    if input('Want another random number?(Y/N)' ).lower() == 'n':
        break
    print(choices.pop())

# Made by Montana Mendy 
