magicians = ['amy', 'zipper', 'bob', 'jenny', 'ray']
print(f"The first three items in the list are: {magicians[:3]}")
print(f"Three items in the middle of the list are: {magicians[1:4]}")
print(f"Last three items of the list are: {magicians[-3:]}")

new_magicians = magicians[:]

new_magicians.append('Max')
for magician in magicians:
    print(magician)

for magician in new_magicians:
    print(magician)