foods = ('rice', 'noodle', 'milk', 'pizza', 'coke')

for food in foods:
    print(food)

#Should return an error as tuple doesn't support motification directly
foods[0] = 'spegati'

#To modify a turple
foods = ('rice', 'noodle', 'pepsi', 'burger', 'coke')