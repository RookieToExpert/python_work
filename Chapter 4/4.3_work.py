# for number in range(1, 21):
#     print(f"Count: {number}")

# for number in range(1, 1_000_000):
#     print(f"Count: {number}")

numbers = [number for number in range(1, 1_000_001)]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

for number in range(1, 20, 2):
    print(number)

for number in range(3, 30, 3):
    print(number)

for number in range(1, 10):
    print(number**3)

cubes = [number**3 for number in range(1,10)]
print(cubes)