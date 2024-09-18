#name of the NBA players
name = ['Lebron', 'Michael', 'Johnson', 'Kobe', 'Dunken']
# print the list varibles
# print(name)
print(name[0].lower())
print(name[-1].lower())
#assign a new message string value to present a message
message = f"My favorite player is {name[0].upper()}."
print(message)

#modify a name in the list
name[-1] = 'Iverson'
print(name)

#add a new element to the list, append can used for a empty list as well.
name.append('Shake')
print(name)

#Insearting elements into a list
name.insert(6, 'Kyir')
print(name)

#Removing elements from the list
del name[4]
print(name)

#Using Pop() to remove item
worst = name.pop()
print(name)
print(worst)
print(f"The worst player on the list is {worst}..")
best = name.pop(0)
print(best)
message = f"The best player on the list is {best}!"
print(message)

#Removing a item by value
center = 'Shake'
name.remove(center)
print(name)
print(f"\n{center.upper()} is one of the greatest Center in the history!")