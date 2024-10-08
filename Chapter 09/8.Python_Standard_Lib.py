#The Python standard library is a set of modules included with every Python installation.
from random import randint
print(randint(1, 8))

from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)