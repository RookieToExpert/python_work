for value in range(1, 5):
    print(value)

numbers = list(range(1,7))
print(numbers)

even_numbers = list(range(2, 10, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

#List comprehensions same as above
squares = [value**2 for value in range(1,11)]
print(squares)


print(min(squares))
print(max(squares))
print(sum(squares))
