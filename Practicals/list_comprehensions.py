
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [number for number in numbers if number % 2 == 0]
squared_numbers = [number ** 2 for number in numbers]

print("Even numbers:", even_numbers)
print("Squared numbers:", squared_numbers)
