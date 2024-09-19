#Create a simple dictionary which is a key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#Can assign the value in the dictionary to another new value
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

#Add new pieces to directory
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#Can create a an empty dictionary
alien = {}
alien['UserAccount1'] = 'ray'
alien['UserAccount2'] = 'jenny'
print(alien)

#Modify an value in dictionary
alien['UserAccount1'] = 'new_ray'
print(alien['UserAccount1'])

#Move the alien to the right.
#Determine how far to move the alien based on its current speed
alien_0['speed'] = 'medium'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

#Delete a value in the dictionary
del alien_0['speed']
print(alien_0)