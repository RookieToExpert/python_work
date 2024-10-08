players = ['charles', 'bobs', 'mike', 'john', 'amy']
print(players[0:3])
print(players[1:4])
print(players[:3])
print(players[0:])

for player in players[:3]:
    print(player.title())

#Copy a list using slice, if you use list = list will create a softlink of the list but not a new list
friend_players = players[:]
print(friend_players)
